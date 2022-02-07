import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 500, 500)  # x, y, width, high
        self.setWindowTitle('using Images')
        self.user_interface()

    def user_interface(self):
        self.image = QLabel(self)
        self.image.setPixmap(QPixmap('../images/Smiley.jpg'))
        self.image.move(80, 50)
        removebtn = QPushButton('Remove', self)
        removebtn.move(290, 380)
        showbtn = QPushButton('Show', self)
        showbtn.move(210, 380)
        removebtn.clicked.connect(self.rmfunc)
        showbtn.clicked.connect(self.showfunc)

        self.show()  # show the window to the user

    def rmfunc(self):
        self.image.close()

    def showfunc(self):
        self.image.show()


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
