import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 350, 550)  # x, y, width, high
        self.setWindowTitle('using labels')
        self.user_interface()

    def user_interface(self):
        text1 = QLabel('Hello Python', self)
        text2 = QLabel('Second Label', self)

        text1.move(50, 50)  # x,y
        text2.move(50, 80)  # y == 80
        self.show()  # show the window to the user


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
