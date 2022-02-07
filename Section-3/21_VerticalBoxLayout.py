import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Vertical Box Layout')
        self.setGeometry(350, 150, 400, 400)  # x, y, width, high
        self.user_interface()

    def user_interface(self):
        vbox = QVBoxLayout()
        btn1 = QPushButton('Save')
        btn2 = QPushButton('Exit')
        btn3 = QPushButton('Hello')
        vbox.addStretch()
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)
        vbox.addStretch()

        self.setLayout(vbox)
        self.show()


def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
