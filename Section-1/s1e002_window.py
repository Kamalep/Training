import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 300, 450)  # x, y, width, high
        self.setWindowTitle('setWindowTitle property = First Title')

        self.show()


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec_())
