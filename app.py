import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QTextEdit, QVBoxLayout
from PyQt6.QtGui import QIcon


class Myapp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Hello World")
        self.setWindowIcon(QIcon("icon.png"))
        self.resize(300, 200)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.inputField = QLineEdit()

        button = QPushButton("Click me", clicked=self.main)

        self.outputField = QTextEdit()

        layout.addWidget(self.inputField)
        layout.addWidget(button)
        layout.addWidget(self.outputField)

    def main(self):
        inputField = self.inputField.text()
        self.outputField.setText(f"hello {inputField}")


app = QApplication(sys.argv)

app.setStyleSheet('''
    QWidget{
        font-size:25px;
    }

    QPushButton{
        font-size:20px;
    }
''')

window = Myapp()
window.show()

app.exec()