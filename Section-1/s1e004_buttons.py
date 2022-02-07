import sys
from PyQt5.QtWidgets import *


class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 350, 350)
        self.setWindowTitle('Using Labels')
        self.user_interface()

    def user_interface(self):
        self.txt = QLabel('Text', self)
        self.txt.move(170, 50)
        enterbtn = QPushButton('Enter', self)
        exitbtn = QPushButton('Exit', self)
        enterbtn.move(100, 80)
        exitbtn.move(200, 80)
        enterbtn.clicked.connect(self.enter_func)
        exitbtn.clicked.connect(self.exit_func)
        self.show()

    def enter_func(self):
        self.txt.setText('You clicked Enter')
        self.txt.resize(150, 20)

    def exit_func(self):
        self.txt.setText('You clicked Exit')
        self.txt.resize(150, 20)


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
