import sys
from PyQt6.QtWidgets import  QApplication,QWidget,QLineEdit,QPushButton,QTextEdit,QVBoxLayout
from PyQt6.QtGui import QIcon

class  Myapp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello World")
        self.setWindowIcon(QIcon("icon.png"))
        self.resize(300,200)
# app = QApplication([])
app = QApplication(sys.argv)

window = Myapp()
window.show()
app.exec()
