import os
import sqlite3
import sys

from PIL import Image
from PyQt5.QtGui import QPixmap, QFont, QIcon  # Add fonts module.
from PyQt5.QtWidgets import *

font = QFont('Times', 14)  # global variable for family and size font.
con = sqlite3.connect('employees.db')
cur = con.cursor()
default_img = 'pfv11.jpg'
person_id = None


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(450, 150, 750, 600)  # x, y, width, high
        self.setWindowTitle('Employees App')
        self.setWindowIcon(QIcon('../images/emicon.png'))

        self.user_interface()
        self.show()

    def user_interface(self):
        self.main_design()
        self.layouts()
        self.get_emp()
        self.display_st_record()

    def main_design(self):
        self.setStyleSheet('font-size:14pt;font-family:Arial  Bold;')
        self.emp_lst = QListWidget(self)
        self.emp_lst.itemClicked.connect(self.single_clicked)
        self.btn_new = QPushButton('New')
        self.btn_new.clicked.connect(self.add_emp)
        self.btn_update = QPushButton('update')
        self.btn_update.clicked.connect(self.update_emp)
        self.btn_delete = QPushButton('Delete')
        self.btn_delete.clicked.connect(self.delete_emp)

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
        self.right_bottom_layout.addWidget(self.btn_update)
        self.right_bottom_layout.addWidget(self.btn_delete)

        self.setLayout(self.main_layout)

    def add_emp(self):
        self.add_emplyee = add_emp_win()
        self.close()

    def get_emp(self):
        query = 'SELECT id,name,surname FROM employees'
        employees = cur.execute(query).fetchall()
        for employee in employees:
            self.emp_lst.addItem(str(employee[0]) + '-' + employee[1] + ' ' + employee[2])

    def display_st_record(self):
        query = "SELECT * FROM employees ORDER BY ROWID ASC LIMIT 1"
        employee = cur.execute(query).fetchone()
        img = QLabel()
        img.setPixmap(QPixmap('../Section-4/Images/' + employee[5]))
        name = QLabel(employee[1])
        surname = QLabel(employee[2])
        phone = QLabel(employee[3])
        email = QLabel(employee[4])
        address = QLabel(employee[6])
        self.left_layout.setVerticalSpacing(12)
        self.left_layout.addRow('', img)
        self.left_layout.addRow('Namae :', name)
        self.left_layout.addRow('Surname :', surname)
        self.left_layout.addRow('Phone :', phone)
        self.left_layout.addRow('Email :', email)
        self.left_layout.addRow('Adreess : ', address)

    def single_clicked(self):
        for i in reversed(range(self.left_layout.count())):
            widget = self.left_layout.takeAt(i).widget()
            if widget is not None:
                widget.deleteLater()
        employee = self.emp_lst.currentItem().text()
        id = employee.split('-')[0]
        query = 'SELECT * FROM employees WHERE id=?'
        person = cur.execute(query, (id,)).fetchone()  # single item tuple=(1,)
        img = QLabel()
        img.setPixmap(QPixmap('../Section-4/Images/' + person[5]))
        name = QLabel(person[1])
        surname = QLabel(person[2])
        phone = QLabel(person[3])
        email = QLabel(person[4])
        address = QLabel(person[6])
        self.left_layout.setVerticalSpacing(12)
        self.left_layout.addRow('', img)
        self.left_layout.addRow('Namae :', name)
        self.left_layout.addRow('Surname :', surname)
        self.left_layout.addRow('Phone :', phone)
        self.left_layout.addRow('Email :', email)
        self.left_layout.addRow('Adreess : ', address)

    def delete_emp(self):
        if self.emp_lst.selectedItems():
            person = self.emp_lst.currentItem().text()
            id = person.split('-')[0]
            msgbox = QMessageBox.question(self, 'Warning', 'Are you sure to delete this person?',
                                          QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if msgbox == QMessageBox.Yes:
                try:
                    query = 'DELETE FROM employees WHERE id=?'
                    cur.execute(query, (id,))
                    con.commit()
                    QMessageBox.information(self, 'Info', 'Person has been deleted ')
                    self.close()
                    self.main = Window()

                except:
                    QMessageBox.information(self, 'Warning!!!', 'Person has not been deleted ')
        else:
            QMessageBox.information(self, 'Info', 'May you select employee to delete ?')

    def update_emp(self):
        global person_id
        if self.emp_lst.selectedItems():
            person = self.emp_lst.currentItem().text()
            person_id = person.split('-')[0]
            self.update_win = UpdateEmployee()
            self.close()

        else:
            QMessageBox.information(self, 'Info', 'May you select employee to update?')


class UpdateEmployee(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('update Emplyees')
        self.setWindowIcon(QIcon('../images/emicon.png'))
        self.setGeometry(450, 150, 350, 600)
        self.user_interface()
        self.show()

    def user_interface(self):
        self.get_person()
        self.main_design()
        self.layouts()

    def closeEvent(self, event):
        self.main = Window()

    def get_person(self):
        global person_id
        query = "SELECT * FROM employees WHERE id=?"
        employee = cur.execute(query, (person_id,)).fetchone()
        self.name = employee[1]
        self.surname = employee[2]
        self.phone = employee[3]
        self.email = employee[4]
        self.address = employee[6]
        self.img = employee[5]

    def main_design(self):
        # Top layout widgets
        self.setStyleSheet('background-color:white;font-size: 14pt;font-family:Times')
        self.title = QLabel('Update Person')
        self.title.setStyleSheet('font-size: 24pt;font-family:Arial Bold;')
        self.img_add = QLabel()
        self.img_add.setPixmap(QPixmap('images/{}'.format(self.img)))
        # Bottom layout widgets
        self.lblname = QLabel('Name :')
        self.name_entry = QLineEdit()
        self.name_entry.setText(self.name)
        self.lblsurname = QLabel('Surname :')
        self.surname_entry = QLineEdit()
        self.surname_entry.setText(self.surname)
        self.lblphone = QLabel('Phone :')
        self.phone_entry = QLineEdit()
        self.phone_entry.setText(self.phone)
        self.lblemail = QLabel('Email :')
        self.email_entry = QLineEdit()
        self.email_entry.setText(self.email)
        self.lblimg = QLabel('Picture :')
        self.btnimg = QPushButton('Browse')
        self.btnimg.setStyleSheet('background-color:Orange;font-family:Times;font-size: 10pt')
        self.btnimg.clicked.connect(self.upload_img)
        self.lbladdress = QLabel('Address :')
        self.address_editor = QTextEdit()
        self.address_editor.setText(self.address)
        self.btn_update = QPushButton('Update')
        self.btn_update.setStyleSheet('background-color:Orange;font-family:Times;font-size: 10pt')
        self.btn_update.clicked.connect(self.update_emp)

    def layouts(self):
        # Creating main layout
        self.main_layout = QVBoxLayout()
        self.top_layout = QVBoxLayout()
        self.bottom_layout = QFormLayout()

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
        self.bottom_layout.addRow(self.lblname, self.name_entry)
        self.bottom_layout.addRow(self.lblsurname, self.surname_entry)
        self.bottom_layout.addRow(self.lblphone, self.phone_entry)
        self.bottom_layout.addRow(self.lblemail, self.email_entry)
        self.bottom_layout.addRow(self.lblimg, self.btnimg)
        self.bottom_layout.addRow(self.lbladdress, self.address_editor)
        self.bottom_layout.addRow("", self.btn_update)
        # sitting main layout for window
        self.setLayout(self.main_layout)

    def update_emp(self):
        global default_img
        global person_id
        name = self.name_entry.text()
        surname = self.surname_entry.text()
        phone = self.phone_entry.text()
        email = self.email_entry.text()
        address = self.address_editor.toPlainText()
        img = default_img
        if name and surname and phone != "":
            try:
                query = "update employees set name=?, surname=?, phone=?,email=?,img=?,address=? WHERE id=?"
                cur.execute(query, (name, surname, phone, email, img, address, person_id))
                con.commit()
                QMessageBox.information(self, "Success", "Person has been updated")
                self.close()
                self.main = Window()
            except:
                QMessageBox.information(self, "Warning", "Person has not been updated")
        else:
            QMessageBox.information(self, "Warning", "Fields can not be empty")

    def upload_img(self):
        global default_img
        size = (128, 128)
        self.filename, ok = QFileDialog.getOpenFileName(self, "Upload Image", "", "Images file (*.jpg *.png)")

        if ok:
            default_img = os.path.basename(self.filename)
            img = Image.open(self.filename)
            img = img.resize(size)
            img.save("images/{}".format(default_img))


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

    def closeEvent(self, event):
        self.main = Window()

    def main_design(self):
        # Top layout widgets
        self.setStyleSheet('background-color:white;font-size: 14pt;font-family:Times')
        self.title = QLabel('Add Person')
        self.title.setStyleSheet('font-size: 24pt;font-family:Arial Bold;')
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
        self.btnimg.setStyleSheet('background-color:Orange;font-family:Times;font-size: 10pt')
        self.btnimg.clicked.connect(self.upload_img)
        self.lbladdress = QLabel('Address :')
        self.address_editor = QTextEdit()
        self.btnadd = QPushButton('Add')
        self.btnadd.setStyleSheet('background-color:Orange;font-family:Times;font-size: 10pt')
        self.btnadd.clicked.connect(self.add_emp)

    def layouts(self):
        # Creating main layout
        self.main_layout = QVBoxLayout()
        self.top_layout = QVBoxLayout()
        self.bottom_layout = QFormLayout()

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
        self.bottom_layout.addRow(self.lblname, self.name_entry)
        self.bottom_layout.addRow(self.lblsurname, self.surname_entry)
        self.bottom_layout.addRow(self.lblphone, self.phone_entry)
        self.bottom_layout.addRow(self.lblemail, self.email_entry)
        self.bottom_layout.addRow(self.lblimg, self.btnimg)
        self.bottom_layout.addRow(self.lbladdress, self.address_editor)
        self.bottom_layout.addRow("", self.btnadd)
        # sitting main layout for window
        self.setLayout(self.main_layout)

    def add_emp(self):
        global default_img
        name = self.name_entry.text()
        surname = self.surname_entry.text()
        phone = self.phone_entry.text()
        email = self.email_entry.text()
        address = self.address_editor.toPlainText()
        img = default_img
        if name and surname and phone != "":
            try:
                query = "INSERT INTO employees (name,surname,phone,email,img,address) VALUES(?,?,?,?,?,?)"
                cur.execute(query, (name, surname, phone, email, img, address))
                con.commit()
                QMessageBox.information(self, "Success", "Person has been added")
                self.close()
                self.main = Window()
            except:
                QMessageBox.information(self, "Warning", "Person has not been added")
        else:
            QMessageBox.information(self, "Warning", "Fields can not be empty")

    def upload_img(self):
        global default_img
        size = (128, 128)
        self.filename, ok = QFileDialog.getOpenFileName(self, "Upload Image", "", "Images file (*.jpg *.png)")

        if ok:
            default_img = os.path.basename(self.filename)
            img = Image.open(self.filename)
            img = img.resize(size)
            img.save("images/{}".format(default_img))


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
