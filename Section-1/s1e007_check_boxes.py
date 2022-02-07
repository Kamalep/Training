import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 500, 500)  # x, y, width, high
        self.setWindowTitle('using Check boxes')
        self.user_interface()

    def user_interface(self):
        self.name = QLineEdit(self)
        self.surname = QLineEdit(self)
        self.name.move(150, 50)
        self.surname.move(150, 80)
        self.name.setPlaceholderText('Enter your name')
        self.surname.setPlaceholderText('Enter your surname')
        self.remmber = QCheckBox('remmber me', self)
        self.remmber.move(150, 110)
        submitbtn = QPushButton('Submit', self)
        submitbtn.move(210, 140)
        submitbtn.clicked.connect(self.submit)

        self.show()  # show the window to the user

    def submit(self):
        if self.remmber.isChecked():
            print('name is', self.name.text())
            print('sername is', self.surname.text())
        else:
            print('Remmber me isn\'t Checked')


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
