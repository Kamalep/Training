import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont  # Add fonts module.

font = QFont('Times', 14)  # global variable for family and size font.


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(250, 150, 500, 500)  # x, y, width, high
        self.setWindowTitle('Using Text editor')
        self.UI()

    def UI(self):
        self.editor = QTextEdit(self)
        self.editor.move(150, 80)
        self.editor.setAcceptRichText(True)  # allow to adding text format such as Blod,underline...
        btn = QPushButton('Send', self)
        btn.move(330, 280)
        btn.clicked.connect(self.getValue)

        self.show()

    def getValue(self):
        txt = self.editor.toPlainText()
        print(txt)


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
