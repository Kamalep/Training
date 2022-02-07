import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(250, 150, 500, 500)  # x, y, width, high
        self.setWindowTitle('using Combo box')
        self.user_interface()

    def user_interface(self):
        self.combo = QComboBox(self)
        self.combo.move(150, 100)
        btn = QPushButton('Save', self)
        btn.move(150, 140)
        btn.clicked.connect(self.getValue)
        self.combo.addItem('Python')  # add one item
        self.combo.addItems(['C', 'C++', 'C#', 'Jave', 'JaveScript', 'PHP'])  # add multi items
        lst = ['Kamal', 'Rafa', 'Dana', 'Abdalaziz']
        for name in lst:
            self.combo.addItem(name)
        for number in range(20, 50):
            self.combo.addItem(str(number))  # if you don't cast to  string from integer. it'll make error

        self.show()  # show the window to the user

    def getValue(self):
        value = self.combo.currentText()
        print(value)


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
