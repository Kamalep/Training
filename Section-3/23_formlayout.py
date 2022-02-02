import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Form Layout')
        self.setGeometry(350, 150, 400, 400)  # x, y, width, high
        self.UI()

    def UI(self):
        formlayout = QFormLayout()
        # formlayout.setRowWrapPolicy(QFormLayout.WrapAllRows) # put label up edited line
        name_txt = QLabel('Name :')
        name_input = QLineEdit()
        name_input.setPlaceholderText('Enter name')
        password_txt = QLabel('Password :')
        password_input = QLineEdit()
        password_input.setPlaceholderText('Enter Password')
        hbox = QHBoxLayout()
        hbox.addStretch()
        hbox.addWidget(QPushButton('Enter'))
        hbox.addWidget(QPushButton('Exit'))
        hbox1 = QHBoxLayout()
        hbox1.addWidget(QLineEdit())
        hbox1.addWidget(QLineEdit())
        hbox1.addWidget(QLineEdit())

        formlayout.addRow(name_txt, hbox1)
        formlayout.addRow(password_txt, password_input)
        formlayout.addRow(QLabel('Country :'), QComboBox())
        # formlayout.addRow(QPushButton('Enter'), QPushButton('Exit'))
        formlayout.addRow(hbox)
        self.setLayout(formlayout)

        self.show()


def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
