import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont  # Add fonts module.

font = QFont('Times', 16)  # global variable for family and size font.


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(250, 150, 500, 500)  # x, y, width, high
        self.setWindowTitle('Using Spin Box')
        self.UI()

    def UI(self):
        self.spinBox = QSpinBox(self)
        self.spinBox.move(150, 100)
        self.spinBox.setFont(font)  # use variable font as parameter

        # self.spinBox.setMinimum(20)  # limit minimum items ---> we can use setRange for min&max items
        # self.spinBox.setMaximum(200)  # limit maximum items

        self.spinBox.setRange(20, 30)
        # self.spinBox.setPrefix('£')  # Add prefix such as currency symbol
        self.spinBox.setSuffix(' cm')  # Add suffix
        self.spinBox.setSingleStep(2)  # increase value (n)
        # self.spinBox.valueChanged.connect(self.getValue)
        btn = QPushButton('Send', self)
        btn.move(150, 140)
        btn.clicked.connect(self.getValue)

        self.show()  # show the window to the user

    def getValue(self):
        value = self.spinBox.value()
        print(value)


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
