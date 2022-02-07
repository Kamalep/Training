import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Tab Widget')
        self.setGeometry(350, 150, 600, 600)  # x, y, width, high
        self.user_interface()

    def user_interface(self):
        mainlayout = QVBoxLayout()
        self.tabs = QTabWidget()

        self.btn_exit = QPushButton('Exit')
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()

        self.tabs.addTab(self.tab1, '1st')
        self.tabs.addTab(self.tab2, '2nd')
        self.tabs.addTab(self.tab3, '3rd')

        mainlayout.addWidget(self.tabs)
        mainlayout.addWidget(self.btn_exit)
        self.setLayout(mainlayout)

        # K_Widgets
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()

        self.txt = QLabel('Hello Python')
        self.btn1 = QPushButton('1st Tab')
        self.btn1.clicked.connect(self.btn1_func)
        self.btn2 = QPushButton('2nd Tab')
        self.btn3 = QPushButton('3rd Tab')

        vbox.addWidget(self.txt)
        vbox.addWidget(self.btn1)
        hbox.addWidget(self.btn2)  # X-axis
        hbox.addStretch()
        self.tab1.setLayout(vbox)
        self.tab2.setLayout(hbox)

        self.show()

    def btn1_func(self):
        self.txt.setText('Button 1 is Active')


def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
