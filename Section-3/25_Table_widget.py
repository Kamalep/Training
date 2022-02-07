import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Table Widget')
        self.setGeometry(350, 150, 400, 400)  # x, y, width, high
        self.user_interface()

    def user_interface(self):
        vbox = QVBoxLayout()
        self.table = QTableWidget()
        btn = QPushButton('Get')
        self.table.setRowCount(5)
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderItem(0, QTableWidgetItem('Name'))
        self.table.setHorizontalHeaderItem(1, QTableWidgetItem('Sername'))
        self.table.setHorizontalHeaderItem(2, QTableWidgetItem('Adress'))
        self.table.setHorizontalHeaderItem(3, QTableWidgetItem('Age'))
        self.table.setItem(0, 0, QTableWidgetItem('First'))  # Row,Column (0, 0)
        self.table.setItem(1, 1, QTableWidgetItem('1,1'))  # Row,Column (1,1)
        self.table.setItem(2, 1, QTableWidgetItem('2,1'))  # Row,Column (2, 1)
        self.table.setItem(3, 2, QTableWidgetItem('3,2'))  # Row,Column (3, 2)
        self.table.setItem(4, 3, QTableWidgetItem('Last'))  # Row,Column (4, 3)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)  # not allow edit cell
        btn.clicked.connect(self.get_value)
        self.table.doubleClicked.connect(self.double_clicked)
        # self.table.horizontalHeader().hide()
        # self.table.verticalHeader().hide()
        vbox.addWidget(self.table)
        vbox.addWidget(btn)
        self.setLayout(vbox)

        self.show()

    def double_clicked(self):
        for item in self.table.selectedItems():
            print(item.text(), item.row(), item.column())

    def get_value(self):
        for item in self.table.selectedItems():
            print(item.text(), item.row(), item.column())


def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
