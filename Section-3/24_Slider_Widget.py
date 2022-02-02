import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Slider Widget')
        self.setGeometry(350, 150, 600, 500)  # x, y, width, high
        self.UI()

    def UI(self):
        vbox = QVBoxLayout()
        # self.slider = QSlider()
        # self.slider.setMaximum(100)
        # self.slider.setMinimum(20)
        # self.slider.setTickInterval(10)
        # self.slider.setTickPosition(QSlider.TicksRight)
        # vbox.addWidget(self.slider)

        self.vslider = QSlider(Qt.Horizontal)
        self.vslider.setMaximum(90)
        self.vslider.setMinimum(10)
        self.vslider.setTickInterval(10)
        self.vslider.valueChanged.connect(self.get_value)
        self.vslider.setTickPosition(QSlider.TicksAbove)

        self.txt1 = QLabel('0')
        self.txt1.setAlignment(Qt.AlignCenter)
        self.txt2 = QLabel('Hello Python')
        vbox.addStretch()
        vbox.addWidget(self.txt1)
        vbox.addWidget(self.txt2)
        vbox.addWidget(self.vslider)

        self.setLayout(vbox)

        self.show()

    def get_value(self):
        val = self.vslider.value()
        # print(val)
        self.txt1.setText(str(val))
        fontsize = val
        font = QFont('Times', fontsize)
        self.txt2.setFont(font)


def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
