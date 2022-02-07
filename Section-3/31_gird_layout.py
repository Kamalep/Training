import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Grid Layout')
        self.setGeometry(350, 150, 600, 600)  # x, y, width, high
        self.user_interface()

    def user_interface(self):
        self.grid_layout = QGridLayout()
        # btn1 = QPushButton('Botton 1')
        # btn2 = QPushButton('Botton 2')
        # btn3 = QPushButton('Botton 3')
        # btn4 = QPushButton('Botton 4')
        #
        # self.grid_layout.addWidget(btn1,0,0)
        # self.grid_layout.addWidget(btn2,0,1)
        # self.grid_layout.addWidget(btn3,1,0)
        # self.grid_layout.addWidget(btn4,1,1)

        for r in range(0, 3):
            for c in range(0, 3):
                btn = QPushButton('Botton {}{}'.format(r, c))
                btn.clicked.connect(self.clickedme)
                self.grid_layout.addWidget(btn, r, c)

        self.setLayout(self.grid_layout)
        self.show()

    def clickedme(self):
        btn_id = self.sender().text()
        if btn_id == 'Botton 00 was clicked':
            print('Botton 00')
        elif btn_id == 'Botton 01':
            print('Botton 01 was clicked')


def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
