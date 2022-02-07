import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 500, 500)  # x, y, width, high
        self.setWindowTitle('List Widget')
        self.user_interface()

    def user_interface(self):
        self.addRecord = QLineEdit(self)
        self.addRecord.move(100, 50)
        self.lstWidget = QListWidget(self)
        self.lstWidget.move(100, 80)
        ################# Buttons ########################
        btnAdd = QPushButton('Add', self)
        btnAdd.move(360, 80)
        btnAdd.clicked.connect(self.funcAdd)

        btnDelete = QPushButton('Delete', self)
        btnDelete.move(360, 110)
        btnDelete.clicked.connect(self.funcDelete)

        btnGet = QPushButton('Get', self)
        btnGet.move(360, 140)
        btnGet.clicked.connect(self.funcGet)

        btnDeleteAll = QPushButton('Delete All', self)
        btnDeleteAll.move(360, 170)
        btnDeleteAll.clicked.connect(self.funcDeleteAll)

        btnEx = QPushButton('Exit', self)
        btnEx.move(360, 200)
        btnEx.clicked.connect(self.funcEx)

        #########################################
        lstItimes = ['One', 'Two', 'Three', 'Four']
        self.lstWidget.addItems(lstItimes)  # add multi items
        self.lstWidget.addItem('Twenty')  # add one item

        ##### use loop to add items #####
        # for number in range(5, 12):
        #     self.lstWidget.addItem(str(number))

        self.show()

    def funcAdd(self):
        val = self.addRecord.text()
        self.lstWidget.addItem(val)
        self.addRecord.setText('')

    def funcDelete(self):
        idx = self.lstWidget.currentRow()
        print(idx)
        self.lstWidget.takeItem(idx)

    def funcDeleteAll(self):
        self.lstWidget.clear()

    def funcGet(self):
        val = self.lstWidget.currentItem().text()
        print(val)
    def funcEx(self):
        sys.exit()


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
