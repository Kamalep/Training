import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Vertical and Horizontal Layout')
        self.setGeometry(350, 150, 400, 400)  # x, y, width, high
        self.UI()

    def UI(self):
        mainlayout = QVBoxLayout()
        toplayout = QHBoxLayout()
        bottomlayout = QHBoxLayout()
        mainlayout.addLayout(toplayout)
        mainlayout.addLayout(bottomlayout)
        cbox = QCheckBox()
        rbtn = QRadioButton()
        combo = QComboBox()
        btn1 = QPushButton()
        btn2 = QPushButton()
        toplayout.setContentsMargins(150, 10, 20, 20)  # left, top, right, bottom
        toplayout.addWidget(combo)
        toplayout.addWidget(cbox)
        toplayout.addWidget(rbtn)
        bottomlayout.setContentsMargins(150, 10, 150, 10)  # left, top, right, bottom
        bottomlayout.addWidget(btn1)
        bottomlayout.addWidget(btn2)
        self.setLayout(mainlayout)

        self.show()


def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
