import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(250, 150, 500, 500)  # x, y, width, high
        self.setWindowTitle('using Radio Buttons')
        self.UI()

    def UI(self):
        self.name = QLineEdit(self)
        self.name.move(150, 50)
        self.name.setPlaceholderText('Enter name')
        self.surname = QLineEdit(self)
        self.surname.move(150, 80)
        self.surname.setPlaceholderText('Enter surname')

        self.male = QRadioButton('Male', self)
        self.male.move(150, 110)
        self.male.setChecked(True)
        self.female = QRadioButton('Female', self)
        self.female.move(200, 110)

        btn = QPushButton('Submit', self)
        btn.move(250, 140)
        btn.clicked.connect(self.getValues)

        self.show()  # show the window to the user

    def getValues(self):
        name = self.name.text()
        surname = self.surname.text()

        if self.male.isChecked():
            print(name, surname, 'is Male')
        else:
            print(f'{name} {surname} is Female')


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
