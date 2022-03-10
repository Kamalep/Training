import sqlite3
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QFont, QIcon  # Add fonts module.

font = QFont('Times', 14)  # global variable for family and size font.
con = sqlite3.connect('emp.db')
cur = con.cursor()


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(450, 150, 750, 600)  # x, y, width, high
        self.setWindowTitle('Employees App')
        self.setWindowIcon(QIcon('../images/emicon.png'))

        self.user_interface()

    def user_interface(self):
        self.main_design()
        self.layouts()

        self.show()

    def main_design(self):
        self.emp_lst = QListWidget(self)
        self.btn_new = QPushButton('New')
        self.btn_new.clicked.connect(self.add_emp)
        self.btn_updata = QPushButton('Updata')
        self.btn_delete = QPushButton('Delete')

    def layouts(self):
        # add layouts
        self.main_layout = QHBoxLayout()

        self.left_layout = QFormLayout()

        self.right_main_layout = QVBoxLayout()

        self.right_top_layout = QHBoxLayout()
        self.right_bottom_layout = QHBoxLayout()

        # add child layouts
        self.right_main_layout.addLayout(self.right_top_layout)
        self.right_main_layout.addLayout(self.right_bottom_layout)

        self.main_layout.addLayout(self.left_layout, 40)
        self.main_layout.addLayout(self.right_main_layout, 50)
        # add widgets to layouts
        self.right_top_layout.addWidget(self.emp_lst)
        self.right_bottom_layout.addWidget(self.btn_new)
        self.right_bottom_layout.addWidget(self.btn_updata)
        self.right_bottom_layout.addWidget(self.btn_delete)

        self.setLayout(self.main_layout)

    def add_emp(self):
        self.add_emplyee = add_emp_win()
        self.close()


class add_emp_win(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Add Emplyees')
        self.setWindowIcon(QIcon('../images/emicon.png'))
        self.setGeometry(450, 150, 350, 600)
        self.user_interface()
        self.show()

    def user_interface(self):
        self.main_design()
        self.layouts()

    def main_design(self):
        # Top layout widgets
        self.title = QLabel('Add Person')
        self.title.setStyleSheet('font-size: 24pt;font-family:Arial Bold;background-color:red')
        self.img_add = QLabel()
        self.img_add.setPixmap(QPixmap('../images/addmember1200.png'))
        # Bottom layout widgets
        self.lblname = QLabel('Name :')
        self.name_entry = QLineEdit()
        self.name_entry.setPlaceholderText('Enter Employee name')
        self.lblsurname = QLabel('Surname :')
        self.surname_entry = QLineEdit()
        self.surname_entry.setPlaceholderText('Enter Employee surname')
        self.lblphone = QLabel('Phone :')
        self.phone_entry = QLineEdit()
        self.phone_entry.setPlaceholderText('Enter Employee Phone namber')
        self.lblemail = QLabel('Email :')
        self.email_entry = QLineEdit()
        self.email_entry.setPlaceholderText('Enter Employee Email')
        self.lblimg = QLabel('Picture :')
        self.btnimg = QPushButton('Browse')
        self.lbladdress = QLabel('Address :')
        self.address_editor = QTextEdit()
        self.btnadd = QPushButton('Add')

    def layouts(self):
        # Creating main layout
        self.main_layout = QVBoxLayout()
        self.top_layout = QVBoxLayout()
        self.bottom_layout = QVBoxLayout()

        # Creating child layout to main layout
        self.main_layout.addLayout(self.top_layout)
        self.main_layout.addLayout(self.bottom_layout)
        # Adding Widget top layout
        # Top layout
        self.top_layout.addStretch()
        self.top_layout.addWidget(self.title)
        self.top_layout.addWidget(self.img_add)
        self.top_layout.addStretch()
        self.top_layout.setContentsMargins(120, 20, 10, 30)  # left, top , right, bottom
        # Bottom layout
        self.bottom_layout.add
        self.bottom_layout.addRow(self.lblname, self.name_entry)
        self.bottom_layout.addRow(self.lblsurname, self.surname_entry)
        self.bottom_layout.addRow(self.lblphone, self.phone_entry)
        self.bottom_layout.addRow(self.lblemail, self.email_entry)
        self.bottom_layout.addRow(self.lblimg, self.btnimg)
        self.bottom_layout.addRow(self.lbladdress, self.address_editor)
        self.bottom_layout.addRow(self.lblemail, self.email_entry)
        self.bottom_layout.addRow("", self.btnadd)
        sitting main layout for window
        self.setLayout(self.main_layout)


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
