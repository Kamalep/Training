import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer

count = 0


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(350, 150, 500, 500)  # x, y, width, high
        self.setWindowTitle('ProgressBar Widget')
        self.user_interface()

    def user_interface(self):
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        self.progressbar = QProgressBar()
        btn_start = QPushButton('Start')
        btn_start.clicked.connect(self.timer_start)
        btn_stop = QPushButton('Stop')
        btn_stop.clicked.connect(self.timer_stop)
        self.timer = QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.run_progressbar)
        vbox.addWidget(self.progressbar)
        vbox.addLayout(hbox)
        hbox.addWidget(btn_start)
        hbox.addWidget(btn_stop)

        self.setLayout(vbox)

        self.show()

    def run_progressbar(self):
        global count
        count += 1
        print(count)
        self.progressbar.setValue(count)
        if count == 100: self.timer.stop()

    def timer_start(self):
        self.timer.start()

    def timer_stop(self):
        self.timer.stop()
        # count = 0
        # self.progressbar.setValue(0)


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
