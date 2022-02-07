import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont  # Add fonts module.
from PyQt5.QtCore import QTimer

font = QFont('Times', 14)  # global variable for family and size font.


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(250, 150, 350, 350)  # x, y, width, high
        self.setWindowTitle('Timer Widget')
        self.user_interface()

    def user_interface(self):
        self.colorLabel = QLabel(self)
        self.colorLabel.resize(250, 250)
        self.colorLabel.setStyleSheet('background-color:red')
        self.colorLabel.move(50, 20)
        ############### Buttons ###############
        btnStart = QPushButton('Start', self)
        btnStart.move(180, 280)
        btnStart.clicked.connect(self.start)
        #btnStart.setStyle()
        btnStop = QPushButton('Stop', self)
        btnStop.move(90, 280)
        btnStop.clicked.connect(self.stop)
        ############### timer ###############
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.changeColor)
        self.value = 0

        self.show()

    def start(self):
        self.timer.start()

    def stop(self):
        self.timer.stop()

    def changeColor(self):
        if self.value == 0:
            self.colorLabel.setStyleSheet('background-color:black')
            self.value = 1
        elif self.value == 1:
            self.colorLabel.setStyleSheet('background-color:blue')
            self.value = 2
        else :
            self.colorLabel.setStyleSheet('background-color:red')
            self.value = 0


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
