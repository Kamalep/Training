import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont  # Add fonts module.

font = QFont('Times', 12)  # global variable for family and size font.


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(250, 150, 500, 500)  # x, y, width, high
        self.setWindowTitle('using MessageBox Widget')
        self.UI()

    def UI(self):
        btn = QPushButton('Click ME:', self)
        btn.move(200, 150)
        # we change button font
        btn.setFont(font)  # use global variable font
        btn.clicked.connect(self.MsgBox)
        self.show()  # show the window to the user

    def MsgBox(self):
        #####  MessageBox.question  #####
        # mbox = QMessageBox.question(self, 'Warning !!', 'Are you sure to exit ?',
        #                             QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel,
        #                             QMessageBox.No)  # title , Massage , ADD(Yes,NO,Cancel) Buttons , Fouce No bottons
        # if mbox == QMessageBox.Yes:
        #     print('Exit')
        #     sys.exit()
        # elif mbox == QMessageBox.No:
        #     print('NO')
        # elif mbox == QMessageBox.Cancel:
        #     print('Cancle')

        #####  MessageBox.Information  #####
        mbox = QMessageBox.information(self, "Information",
                                       "You are Logged Out!")  # we don't need yes,no,cancel buttons


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
