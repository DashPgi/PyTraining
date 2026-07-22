import os
import sys
import json
from dotenv import load_dotenv
from openai import OpenAI

from PyQt6.QtCore import Qt, QPointF, QRectF, QObject, QThread, pyqtSignal
from PyQt6.QtGui import QColor, QBrush, QPen, QPainterPath, QFont, QPainter
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout,
    QGraphicsView, QGraphicsScene, QGraphicsItem, QGraphicsRectItem,
    QGraphicsEllipseItem, QGraphicsPathItem, QGraphicsTextItem,
    QPushButton, QLabel, QTextEdit, QLineEdit, QComboBox, QSpinBox,
    QDialog, QDialogButtonBox, QFormLayout, QSplitter, QMessageBox,
    QFileDialog, QScrollArea, QGroupBox, QSizePolicy, QMenu
)

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
MODEL = os.getenv("MODEL", "anthropic/claude-sonnet-5")
MAX_TOKENS = int(os.getenv("MAX_TOKENS", "4000"))

client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=OPENROUTER_API_KEY)

NODE_DEFS = {
    "trigger_message": {"label": "Message Received", "color": "#5fc9d1", "inputs": 0, "outputs": 1,
                         "fields": [("note", "Note (optional)", "text")]},
    "trigger_command": {"label": "Command", "color": "#5fc9d1", "inputs": 0, "outputs": 1,
                         "fields": [("command", "Command name (e.g. start)", "text")]},
    "condition": {"label": "Condition (If)", "color": "#c9a15f", "inputs": 1, "outputs": 2,
                  "out_labels": ["Yes", "No"],
                  "fields": [("expr", "Condition", "multiline")]},
    "switch": {"label": "Switch", "color": "#c9a15f", "inputs": 1, "outputs": 4,
               "out_labels": ["Case 1", "Case 2", "Case 3", "Default"],
               "fields": [("cases", "Case values (one per line, matches Case 1/2/3 order)", "multiline")]},
    "delay": {"label": "Delay", "color": "#c9a15f", "inputs": 1, "outputs": 1,
              "fields": [("seconds", "Delay duration (seconds)", "number")]},
    "merge": {"label": "Merge", "color": "#c9a15f", "inputs": 3, "outputs": 1,
              "fields": [("note", "Note (optional)", "text")]},
    "split": {"label": "Split", "color": "#c9a15f", "inputs": 1, "outputs": 3,
              "out_labels": ["Path 1", "Path 2", "Path 3"],
              "fields": [("note", "Note (optional)", "text")]},
    "send_message": {"label": "Send Message", "color": "#e8935a", "inputs": 1, "outputs": 1,
                      "fields": [("text", "Message text", "multiline")]},
    "send_buttons": {"label": "Buttons / Menu", "color": "#e8935a", "inputs": 1, "outputs": 1,
                      "fields": [("buttons", "Buttons (one per line)", "multiline")]},
    "save_data": {"label": "Save Data", "color": "#8fc95f", "inputs": 1, "outputs": 1,
                  "fields": [("target", "Storage location", "select", ["JSON file", "SQLite database", "Google Sheet"]),
                             ("field", "What to save", "text")]},
    "read_data": {"label": "Read Data", "color": "#8fc95f", "inputs": 1, "outputs": 1,
                  "fields": [("source", "Source", "select", ["JSON file", "SQLite database", "Google Sheet"])]},
    "http_request": {"label": "API Request", "color": "#8fc95f", "inputs": 1, "outputs": 1,
                      "fields": [("url", "API URL", "text"), ("method", "Method", "select", ["GET", "POST"])]},
    "ai_response": {"label": "AI Response", "color": "#a05fc9", "inputs": 1, "outputs": 1,
                     "fields": [("prompt", "Instruction to the AI (system prompt)", "multiline")]},
    "end": {"label": "End Flow", "color": "#5a6270", "inputs": 1, "outputs": 0, "fields": []},
}

CATEGORIES = [
    ("Trigger", ["trigger_message", "trigger_command"]),
    ("Logic", ["condition", "switch", "delay"]),
    ("Flow Control", ["merge", "split"]),
    ("Action", ["send_message", "send_buttons"]),
    ("Data", ["save_data", "read_data", "http_request"]),
    ("AI", ["ai_response"]),
    ("End", ["end"]),
]

FLOW_BUILD_PROMPT = """
You are an expert Python developer specialized in the python-telegram-bot library.
Your input is a JSON object with two parts:
- flow: a visual flow (nodes and links) the user built by dragging and connecting nodes
- extra_prompt: free-form user notes about the whole bot (may be empty)

Possible node types: trigger_message, trigger_command, condition, switch, delay,
merge, split, send_message, send_buttons, save_data, read_data, http_request,
ai_response, end

Notes on special node types:
- condition: 2 outputs (out0 = Yes, out1 = No)
- switch: multiple outputs (out0..out2 = cases in order given in the "cases" field,
  out3 = default/fallback when no case matches)
- merge: multiple inputs (in0, in1, in2...) converging into a single continuation —
  treat it as "whichever path arrives here, continue with the same next step"
- split: 1 input, multiple outputs (out0, out1, out2...) that should ALL run
  (fan-out to parallel actions, not a conditional branch)

Your task:
1. Follow the links to reconstruct the execution flow.
2. Generate complete, runnable python-telegram-bot (v20+) code implementing it.
3. Use real if/elif/else for condition and switch nodes.
4. Use InlineKeyboardMarkup for send_buttons nodes.
5. For save_data/read_data, implement a simple JSON file store unless another
   target is specified.
6. For ai_response, use an OpenAI-compatible client (e.g. OpenRouter).
7. If extra_prompt has extra notes (brand name, tone, rules), apply them too.
8. Output ONLY the complete Python code (inside a ```python ... ``` block),
   with at most 2 lines of explanation before it.
"""


class InsufficientCreditsError(Exception):
    pass


class ModelUnavailableError(Exception):
    pass


class ModelEmptyResponseError(Exception):
    pass


def ask_model(system_prompt: str, user_content: str) -> str:
    try:
        response = client.chat.completions.create(
            model=MODEL,
            max_tokens=MAX_TOKENS,
            temperature=0.3,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_content},
            ],
        )
    except Exception as e:
        msg = str(e)
        if "402" in msg or "more credits" in msg or "afford" in msg:
            raise InsufficientCreditsError(msg) from e
        if "404" in msg or "unavailable" in msg.lower() or "use this slug instead" in msg:
            raise ModelUnavailableError(msg) from e
        raise

    choice = response.choices[0]
    content = choice.message.content
    if not content:
        reason = getattr(choice, "finish_reason", "unknown")
        raise ModelEmptyResponseError(f"The model returned an empty response — stop reason: {reason}.")

    content = content.strip()
    if getattr(choice, "finish_reason", None) == "length":
        content += "\n\n# Warning: this output may be truncated due to the MAX_TOKENS limit."
    return content


def extract_code(text: str) -> str:
    stripped = text.strip()
    if "```" in stripped:
        parts = stripped.split("```")
        for part in parts[1::2]:
            code = part
            if code.startswith("python"):
                code = code[len("python"):]
            code = code.strip()
            if code:
                return code
    return stripped


class Port(QGraphicsEllipseItem):
    RADIUS = 7

    def __init__(self, node, is_output: bool, index: int = 0):
        super().__init__(-self.RADIUS, -self.RADIUS, self.RADIUS * 2, self.RADIUS * 2)
        self.node = node
        self.is_output = is_output
        self.index = index
        self.default_color = QColor("#e8935a") if is_output else QColor("#5fc9d1")
        self.setBrush(QBrush(QColor("#0e1116")))
        self.setPen(QPen(self.default_color, 2))
        self.setZValue(10)
        self.setAcceptHoverEvents(True)

    def hoverEnterEvent(self, event):
        self.setBrush(QBrush(self.default_color))
        super().hoverEnterEvent(event)

    def hoverLeaveEvent(self, event):
        self.setBrush(QBrush(QColor("#0e1116")))
        super().hoverLeaveEvent(event)


class NodeItem(QGraphicsRectItem):
    def __init__(self, node_id: str, node_type: str, on_moved=None, on_configure=None):
        self.node_id = node_id
        self.node_type = node_type
        self.data = {}
        self.on_moved = on_moved
        self.on_configure = on_configure
        defs = NODE_DEFS[node_type]
        self.defs = defs

        width = 190
        n_in = defs["inputs"]
        n_out = defs["outputs"]
        slots = max(n_in, n_out, 1)
        height = max(78, 50 + slots * 30)

        super().__init__(0, 0, width, height)
        self.setBrush(QBrush(QColor("#1d232c")))
        self.setPen(QPen(QColor("#2a323d"), 1.4))
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable, True)
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsSelectable, True)
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemSendsGeometryChanges, True)

        swatch = QGraphicsRectItem(10, 10, 9, 9, self)
        swatch.setBrush(QBrush(QColor(defs["color"])))
        swatch.setPen(QPen(Qt.PenStyle.NoPen))

        title = QGraphicsTextItem(defs["label"], self)
        title.setDefaultTextColor(QColor("#e7e5e0"))
        f = QFont("Segoe UI", 10, QFont.Weight.DemiBold)
        title.setFont(f)
        title.setPos(24, 4)

        self.summary = QGraphicsTextItem("Double-click to configure", self)
        self.summary.setDefaultTextColor(QColor("#8b93a1"))
        self.summary.setFont(QFont("Segoe UI", 8))
        self.summary.setTextWidth(width - 20)
        self.summary.setPos(10, 28)

        self.in_ports = []
        self.out_ports = []

        in_labels = defs.get("in_labels")
        self.in_ports = self._layout_ports(n_in, width, height, is_output=False, labels=in_labels, x=0)
        out_labels = defs.get("out_labels")
        self.out_ports = self._layout_ports(n_out, width, height, is_output=True, labels=out_labels, x=width)

        # kept for backward compatibility with code that expects a single input port
        self.in_port = self.in_ports[0] if self.in_ports else None

        self.update_summary()

    def _layout_ports(self, count, width, height, is_output, labels, x):
        ports = []
        if count <= 0:
            return ports
        for i in range(count):
            y = height * (i + 1) / (count + 1)
            port = Port(self, is_output, i)
            port.setParentItem(self)
            port.setPos(x, y)
            ports.append(port)
            if labels and i < len(labels):
                lbl = QGraphicsTextItem(labels[i], self)
                lbl.setDefaultTextColor(QColor("#8b93a1"))
                lbl.setFont(QFont("Segoe UI", 7))
                if is_output:
                    lbl.setPos(width - 46, y - 16)
                else:
                    lbl.setPos(10, y - 16)
        return ports

    def update_summary(self):
        filled = {k: v for k, v in self.data.items() if v not in (None, "")}
        if filled:
            text = "\n".join(f"{k}: {str(v)[:26]}" for k, v in filled.items())
        else:
            text = "Double-click to configure"
        self.summary.setPlainText(text)

    def paint(self, painter, option, widget=None):
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        path = QPainterPath()
        rect = self.rect()
        path.addRoundedRect(rect, 8, 8)
        pen = QPen(QColor("#e8935a") if self.isSelected() else QColor("#2a323d"),
                    1.8 if self.isSelected() else 1.4)
        painter.setPen(pen)
        painter.setBrush(self.brush())
        painter.drawPath(path)

    def itemChange(self, change, value):
        if change == QGraphicsItem.GraphicsItemChange.ItemPositionHasChanged and self.on_moved:
            self.on_moved(self)
        return super().itemChange(change, value)

    def mouseDoubleClickEvent(self, event):
        if self.on_configure:
            self.on_configure(self)
        super().mouseDoubleClickEvent(event)

    def contextMenuEvent(self, event):
        menu = QMenu()
        delete_action = menu.addAction("Delete this node")
        action = menu.exec(event.screenPos())
        if action == delete_action:
            self.scene().remove_node(self.node_id)


class LinkItem(QGraphicsPathItem):
    def __init__(self, from_port: Port, to_port: Port):
        super().__init__()
        self.from_port = from_port
        self.to_port = to_port
        self.setPen(QPen(QColor("#5fc9d1"), 2.2))
        self.setZValue(-1)
        self.setAcceptHoverEvents(True)
        self.update_path()

    def update_path(self):
        a = self.from_port.scenePos()
        b = self.to_port.scenePos()
        dx = max(60.0, abs(b.x() - a.x()) / 2)
        path = QPainterPath(a)
        path.cubicTo(a.x() + dx, a.y(), b.x() - dx, b.y(), b.x(), b.y())
        self.setPath(path)

    def touches_node(self, node_id: str) -> bool:
        return self.from_port.node.node_id == node_id or self.to_port.node.node_id == node_id

    def mouseDoubleClickEvent(self, event):
        scene = self.scene()
        if scene and hasattr(scene, "remove_link"):
            scene.remove_link(self)
        event.accept()


class FlowScene(QGraphicsScene):
    SNAP_RADIUS = 28.0

    def __init__(self):
        super().__init__()
        self.setSceneRect(0, 0, 3000, 2000)
        self.setBackgroundBrush(QBrush(QColor("#0e1116")))
        self.nodes = {}
        self.links = []
        self._pending_start = None
        self._temp_line = None
        self._nearest_input = None

    def add_node_item(self, node: NodeItem):
        self.nodes[node.node_id] = node
        self.addItem(node)

    def remove_node(self, node_id: str):
        node = self.nodes.pop(node_id, None)
        if not node:
            return
        for link in [l for l in self.links if l.touches_node(node_id)]:
            self.remove_link(link)
        self.removeItem(node)

    def remove_link(self, link: LinkItem):
        if link in self.links:
            self.links.remove(link)
        if link.scene() is self:
            self.removeItem(link)

    def clear_flow(self):
        for link in list(self.links):
            self.remove_link(link)
        for node_id in list(self.nodes.keys()):
            self.remove_node(node_id)

    def links_touching(self, node: NodeItem):
        return [l for l in self.links if l.touches_node(node.node_id)]

    def _device_transform(self):
        views = self.views()
        return views[0].transform() if views else None

    def mousePressEvent(self, event):
        transform = self._device_transform()
        item = self.itemAt(event.scenePos(), transform) if transform is not None else None
        if isinstance(item, Port) and item.is_output:
            self._pending_start = item
            self._temp_line = QGraphicsPathItem()
            self._temp_line.setPen(QPen(QColor("#e8935a"), 2, Qt.PenStyle.DashLine))
            self._temp_line.setZValue(20)
            self.addItem(self._temp_line)
            event.accept()
            return
        super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self._pending_start is not None:
            a = self._pending_start.scenePos()
            b = event.scenePos()
            dx = max(60.0, abs(b.x() - a.x()) / 2)
            path = QPainterPath(a)
            path.cubicTo(a.x() + dx, a.y(), b.x() - dx, b.y(), b.x(), b.y())
            self._temp_line.setPath(path)
            self._update_nearest_input(b)
            event.accept()
            return
        super().mouseMoveEvent(event)

    def _update_nearest_input(self, pos: QPointF):
        best = None
        best_dist = self.SNAP_RADIUS
        for node in self.nodes.values():
            if node is self._pending_start.node:
                continue
            for in_port in node.in_ports:
                d = ((in_port.scenePos().x() - pos.x()) ** 2 + (in_port.scenePos().y() - pos.y()) ** 2) ** 0.5
                if d < best_dist:
                    best_dist = d
                    best = in_port
        if self._nearest_input is not None and self._nearest_input is not best:
            self._nearest_input.setBrush(QBrush(QColor("#0e1116")))
        if best is not None:
            best.setBrush(QBrush(QColor("#e8935a")))
        self._nearest_input = best

    def mouseReleaseEvent(self, event):
        if self._pending_start is not None:
            if self._nearest_input is not None:
                link = LinkItem(self._pending_start, self._nearest_input)
                self.addItem(link)
                self.links.append(link)
                self._nearest_input.setBrush(QBrush(QColor("#0e1116")))
            if self._temp_line is not None:
                self.removeItem(self._temp_line)
            self._pending_start = None
            self._temp_line = None
            self._nearest_input = None
            event.accept()
            return
        super().mouseReleaseEvent(event)

    def keyPressEvent(self, event):
        if event.key() in (Qt.Key.Key_Delete, Qt.Key.Key_Backspace):
            for item in list(self.selectedItems()):
                if isinstance(item, NodeItem):
                    self.remove_node(item.node_id)
            event.accept()
            return
        super().keyPressEvent(event)


class NodeConfigDialog(QDialog):
    def __init__(self, node: NodeItem, parent=None):
        super().__init__(parent)
        self.node = node
        self.setWindowTitle(node.defs["label"])
        self.setMinimumWidth(360)
        self.inputs = {}

        layout = QFormLayout(self)
        for field in node.defs["fields"]:
            key, label = field[0], field[1]
            ftype = field[2]
            current = node.data.get(key, "")
            if ftype == "multiline":
                w = QTextEdit()
                w.setPlainText(str(current))
                w.setFixedHeight(90)
            elif ftype == "select":
                w = QComboBox()
                w.addItems(field[3])
                if current in field[3]:
                    w.setCurrentText(current)
            elif ftype == "number":
                w = QSpinBox()
                w.setRange(0, 100000)
                try:
                    w.setValue(int(current) if current else 0)
                except ValueError:
                    w.setValue(0)
            else:
                w = QLineEdit(str(current))
            self.inputs[key] = (w, ftype)
            layout.addRow(label, w)

        if not node.defs["fields"]:
            layout.addRow(QLabel("This node has no extra settings."))

        buttons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        )
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addRow(buttons)

    def values(self):
        result = {}
        for key, (w, ftype) in self.inputs.items():
            if ftype == "multiline":
                result[key] = w.toPlainText().strip()
            elif ftype == "select":
                result[key] = w.currentText()
            elif ftype == "number":
                result[key] = w.value()
            else:
                result[key] = w.text().strip()
        return result


class BuildWorker(QObject):
    finished = pyqtSignal(str)
    failed = pyqtSignal(str, str)

    def __init__(self, payload_json: str):
        super().__init__()
        self.payload_json = payload_json

    def run(self):
        try:
            code = ask_model(FLOW_BUILD_PROMPT, self.payload_json)
            self.finished.emit(code)
        except InsufficientCreditsError as e:
            self.failed.emit("credits", str(e))
        except ModelUnavailableError as e:
            self.failed.emit("unavailable", str(e))
        except ModelEmptyResponseError as e:
            self.failed.emit("empty", str(e))
        except Exception as e:
            self.failed.emit("other", str(e))


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bot Wiring — Desktop Edition")
        self.resize(1280, 800)
        self._node_seq = 1
        self._thread = None
        self._worker = None

        self.setStyleSheet(self._stylesheet())

        splitter = QSplitter(Qt.Orientation.Horizontal)
        splitter.addWidget(self._build_left_panel())
        splitter.addWidget(self._build_right_panel())
        splitter.setStretchFactor(0, 3)
        splitter.setStretchFactor(1, 1)
        splitter.setSizes([900, 380])
        self.setCentralWidget(splitter)

    def _stylesheet(self):
        return """
        QMainWindow { background: #0e1116; }
        QWidget { color: #e7e5e0; font-family: 'Segoe UI', sans-serif; font-size: 12.5px; }
        QGroupBox { border: 1px solid #2a323d; border-radius: 8px; margin-top: 10px; padding-top: 8px; }
        QGroupBox::title { subcontrol-origin: margin; left: 10px; color: #8b93a1; font-size: 10.5px; }
        QPushButton { background: #1d232c; border: 1px solid #2a323d; border-radius: 8px; padding: 8px 10px; }
        QPushButton:hover { border-color: #5fc9d1; color: #5fc9d1; }
        QPushButton#exportBtn { background: #e8935a; color: #1a0f08; font-weight: 600; border: none; }
        QPushButton#exportBtn:hover { background: #f0a06c; color: #1a0f08; }
        QPushButton#exportBtn:disabled { background: #7a5138; color: #cbb6a4; }
        QTextEdit, QLineEdit, QComboBox, QSpinBox {
            background: #1d232c; border: 1px solid #2a323d; border-radius: 6px; padding: 6px;
        }
        QGraphicsView { border: none; }
        QLabel#sectionTitle { color: #8b93a1; font-size: 10.5px; font-weight: 600; }
        """

    def _build_left_panel(self):
        container = QWidget()
        v = QVBoxLayout(container)
        v.setContentsMargins(10, 10, 6, 10)

        palette_box = QGroupBox("Nodes (click to add — optional)")
        grid = QGridLayout(palette_box)
        row = 0
        for cat_name, node_types in CATEGORIES:
            cat_label = QLabel(cat_name)
            cat_label.setObjectName("sectionTitle")
            grid.addWidget(cat_label, row, 0, 1, 3)
            row += 1
            col = 0
            for nt in node_types:
                btn = QPushButton(NODE_DEFS[nt]["label"])
                btn.clicked.connect(lambda _, t=nt: self.add_node(t))
                grid.addWidget(btn, row, col)
                col += 1
                if col >= 3:
                    col = 0
                    row += 1
            if col != 0:
                row += 1

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setWidget(palette_box)
        scroll.setMaximumHeight(260)
        v.addWidget(scroll)

        toolbar = QHBoxLayout()
        clear_btn = QPushButton("Clear canvas")
        clear_btn.clicked.connect(self.clear_canvas)
        toolbar.addWidget(clear_btn)
        hint = QLabel("Drag orange (output) to blue (input) to connect · Double-click a node to configure it · Double-click a link to delete it · Right-click a node or select it and press Delete to remove it")
        hint.setWordWrap(True)
        hint.setStyleSheet("color:#8b93a1; font-size:10.5px;")
        toolbar.addWidget(hint, 1)
        v.addLayout(toolbar)

        self.scene = FlowScene()
        self.view = QGraphicsView(self.scene)
        self.view.setRenderHint(QPainter.RenderHint.Antialiasing)
        self.view.setDragMode(QGraphicsView.DragMode.RubberBandDrag)
        self.view.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.view.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.view.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        v.addWidget(self.view, 1)

        return container

    def _build_right_panel(self):
        container = QWidget()
        v = QVBoxLayout(container)
        v.setContentsMargins(6, 10, 10, 10)

        title = QLabel("Prompt / General bot description")
        title.setObjectName("sectionTitle")
        v.addWidget(title)

        self.prompt_edit = QTextEdit()
        self.prompt_edit.setPlaceholderText(
            "Write anything the flow alone doesn't capture — e.g. shop name, "
            "tone of the replies, or special rules.\n\n"
            "The node flow on the left is fully optional: you can build a flow, "
            "write a prompt, or use both together."
        )
        v.addWidget(self.prompt_edit, 1)

        self.status_label = QLabel("")
        self.status_label.setStyleSheet("color:#8b93a1;")
        self.status_label.setWordWrap(True)
        v.addWidget(self.status_label)

        self.export_btn = QPushButton("⚙️ Generate Code")
        self.export_btn.setObjectName("exportBtn")
        self.export_btn.setMinimumHeight(42)
        self.export_btn.clicked.connect(self.on_export_clicked)
        v.addWidget(self.export_btn)

        return container

    def add_node(self, node_type: str):
        node_id = f"n{self._node_seq}"
        self._node_seq += 1
        node = NodeItem(node_id, node_type, on_moved=self.on_node_moved, on_configure=self.on_node_configure)
        center = self.view.mapToScene(self.view.viewport().rect().center())
        node.setPos(center.x() - 95 + (self._node_seq % 5) * 12, center.y() - 40 + (self._node_seq % 4) * 12)
        self.scene.add_node_item(node)

    def on_node_moved(self, node: NodeItem):
        for link in self.scene.links_touching(node):
            link.update_path()

    def on_node_configure(self, node: NodeItem):
        dialog = NodeConfigDialog(node, self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            node.data = dialog.values()
            node.update_summary()

    def clear_canvas(self):
        if not self.scene.nodes:
            return
        confirm = QMessageBox.question(
            self, "Clear canvas", "Delete all nodes and links?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if confirm == QMessageBox.StandardButton.Yes:
            self.scene.clear_flow()

    def build_flow_payload(self) -> dict:
        nodes = []
        for node in self.scene.nodes.values():
            nodes.append({"id": node.node_id, "type": node.node_type, "data": node.data})
        links = []
        for link in self.scene.links:
            links.append({
                "from": {"node": link.from_port.node.node_id, "port": f"out{link.from_port.index}"},
                "to": {"node": link.to_port.node.node_id, "port": f"in{link.to_port.index}"},
            })
        return {
            "flow": {"version": 1, "nodes": nodes, "links": links},
            "extra_prompt": self.prompt_edit.toPlainText().strip(),
        }

    def on_export_clicked(self):
        has_nodes = bool(self.scene.nodes)
        has_prompt = bool(self.prompt_edit.toPlainText().strip())
        if not has_nodes and not has_prompt:
            QMessageBox.warning(
                self, "Nothing to build",
                "Add at least one node OR write a prompt describing the bot (node building is optional)."
            )
            return
        if not OPENROUTER_API_KEY:
            QMessageBox.critical(self, "No API key", "OPENROUTER_API_KEY is not set in your .env file.")
            return

        payload = self.build_flow_payload()
        payload_json = json.dumps(payload, ensure_ascii=False, indent=2)

        self.export_btn.setEnabled(False)
        self.export_btn.setText("Generating code...")
        self.status_label.setText("Talking to the AI model, please wait...")

        self._thread = QThread(self)
        self._worker = BuildWorker(payload_json)
        self._worker.moveToThread(self._thread)
        self._thread.started.connect(self._worker.run)
        self._worker.finished.connect(self.on_build_finished)
        self._worker.failed.connect(self.on_build_failed)
        self._worker.finished.connect(self._thread.quit)
        self._worker.failed.connect(self._thread.quit)
        self._thread.finished.connect(self._reset_export_button)
        self._thread.start()

    def _reset_export_button(self):
        self.export_btn.setEnabled(True)
        self.export_btn.setText("⚙️ Generate Code")

    def on_build_finished(self, code_text: str):
        self.status_label.setText("Code is ready ✅")
        code = extract_code(code_text)
        path, _ = QFileDialog.getSaveFileName(self, "Save bot code", "bot.py", "Python Files (*.py)")
        if not path:
            self.status_label.setText("Code was ready but not saved (you can export again).")
            return
        try:
            with open(path, "w", encoding="utf-8") as f:
                f.write(code)
            QMessageBox.information(self, "Saved", f"Bot code saved to:\n{path}")
        except OSError as e:
            QMessageBox.critical(self, "Save error", str(e))

    def on_build_failed(self, kind: str, message: str):
        if kind == "credits":
            text = (
                "💳 Your OpenRouter account doesn't have enough credits.\n"
                "Visit https://openrouter.ai/settings/credits to top up, "
                "lower MAX_TOKENS in .env, or switch MODEL to a free one."
            )
        elif kind == "unavailable":
            text = (
                f"⚠️ Model \"{MODEL}\" is unavailable or no longer free.\n"
                "Check https://openrouter.ai/models and set an active model in .env."
            )
        elif kind == "empty":
            text = f"The model returned an empty response: {message}\nTry raising MAX_TOKENS or simplifying the flow."
        else:
            text = f"Error: {message}"
        self.status_label.setText("Code generation failed.")
        QMessageBox.warning(self, "Error", text)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()