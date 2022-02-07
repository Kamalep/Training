import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 350, 350)  # x, y, width, high
        self.setWindowTitle('Using QLineEdit')
        self.user_interface()

    def user_interface(self):
        self.nameTextBox = QLineEdit(self)
        self.nameTextBox.move(120, 50)
        self.nameTextBox.setPlaceholderText('Enter Name')
        self.passTextBox = QLineEdit(self)
        self.passTextBox.setEchoMode(QLineEdit.Password)
        self.passTextBox.move(120, 80)
        self.passTextBox.setPlaceholderText('Enter Password')
        btn = QPushButton('Save', self)
        btn.move(180, 110)
        btn.clicked.connect(self.btn_func)

        btnExit = QPushButton('Exit', self)
        btnExit.move(250, 300)
        btnExit.clicked.connect(self.btnExit_func)

        self.show()  # show the window to the user
    def btnExit_func(self):
        self.setWindowTitle('Exit')
    def btn_func(self):
        name = self.nameTextBox.text()
        password = self.passTextBox.text()
        self.setWindowTitle('Hello '+name)
        #print(name,password)

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
