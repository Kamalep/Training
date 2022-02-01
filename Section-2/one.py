import os
import psutil
import sys
from random import randint as rd
from playsound2 import playsound

from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap, QFont, QIcon
from PyQt5.QtWidgets import *

fontbtn = QFont('Chicle-Regular', 14)  # global variable for family and size font.
font = QFont('ComingSoon-Regular', 14)
Paper = '../images/Paper.jpg'
Rook = '../images/Rock.jpg'
Scissors = '../images/Scissors.jpg'
lblCurrenttxt = None
pcScore = 0
palyerScore = 0
count_times = 0


def beep():
    playsound('../Sounds/Win.mp3')
    print('YahoOoOoOoOoOoOo !!!!')


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(350, 150, 550, 500)  # x, y, width, high
        self.setWindowTitle('Rock Paper Scissors Game')
        self.setWindowIcon(QIcon('../images/Vredcolor100.png'))
        self.setStyleSheet("background-color: white")
        self.UI()

    def UI(self):
        # qButtons
        btnExt = QPushButton('Exit', self)
        btnExt.move(442, 442)
        btnExt.setFont(fontbtn)
        btnExt.clicked.connect(self.funcExt)
        btnExt.setStyleSheet("background-color: Red")

        btnStart = QPushButton('Start', self)
        btnStart.move(180, 350)
        btnStart.clicked.connect(self.funcbtnStart)
        btnStart.setFont(font)

        btnStop = QPushButton('Stop', self)
        btnStop.move(270, 350)
        btnStop.clicked.connect(self.funcbtnStop)
        btnStop.setFont(font)

        # klabels
        # lblTitle = QLabel('Rock Paper Scissors Game', self)
        # lblTitle .setFont(font)
        # lblTitle .move(155, 20)

        self.lblComputerScore = QLabel('Computer Score  : 0', self)
        self.lblComputerScore.setFont(font)
        self.lblComputerScore.move(30, 60)

        self.lblPlayerScore = QLabel('Your Score  : 0', self)
        self.lblPlayerScore.setFont(font)
        self.lblPlayerScore.move(320, 60)

        self.lblAttempts = QLabel(self)
        self.lblAttempts.setText(('Attempts : {}'.format(0)))
        self.lblAttempts.setFont(font)
        self.lblAttempts.move(10, 10)
        # lblPlayertxt = QLabel(lblCurrenttxt, self)
        # lblPlayertxt.setFont(font)
        # lblPlayertxt.move(320, 300)
        # lblComputertxt = QLabel(lblCurrenttxt, self)
        # lblComputertxt.setFont(font)
        # lblComputertxt.move(30, 300)

        # kImages
        self.imgPC = QLabel(self)
        self.imgPC.setPixmap(QPixmap(Rook))
        self.imgPC.move(20, 105)
        self.imgPalyer = QLabel(self)
        self.imgPalyer.setPixmap(QPixmap(Paper))
        self.imgPalyer.move(320, 105)

        self.imgVS = QLabel(self)
        self.imgVS.setPixmap(QPixmap('../images/vs.jpg'))
        self.imgVS.move(250, 165)

        ########### kTimer ###########
        self.timer = QTimer(self)
        self.timer.setInterval(80)
        self.timer.timeout.connect(self.playGame)
        self.memory_used()

        self.show()

    # kFunctions

    def playGame(self):
        self.rdPc = rd(1, 3)
        self.rdYou = rd(1, 3)

        if self.rdPc == 1:
            self.imgPC.setPixmap(QPixmap(Paper))
        elif self.rdPc == 2:
            self.imgPC.setPixmap(QPixmap(Scissors))
        elif self.rdPc == 3:
            self.imgPC.setPixmap(QPixmap(Rook))

        if self.rdYou == 1:
            self.imgPalyer.setPixmap(QPixmap(Paper))
        elif self.rdYou == 2:
            self.imgPalyer.setPixmap(QPixmap(Scissors))
        elif self.rdYou == 3:
            self.imgPalyer.setPixmap(QPixmap(Rook))

    def funcExt(self):
        sys.exit()

    def funcbtnStart(self):
        self.timer.start()
       # count_times += 1

    def funcbtnStop(self):
        self.memory_used()
        global pcScore
        global palyerScore
        self.timer.stop()
        beep()
        if self.rdYou == self.rdPc:
            MsgBox = QMessageBox.information(self, 'Information', 'Draw Game !!')
        elif (self.rdPc == 1) and (self.rdYou == 2):
            MsgBox = QMessageBox.information(self, 'Information', 'You Wins !!')
            palyerScore += 1
            self.lblPlayerScore.setText('Your Score : {}'.format(palyerScore))
        elif self.rdPc == 2 and self.rdYou == 3:
            MsgBox = QMessageBox.information(self, 'Information', 'You Wins !!')
            palyerScore += 1
            self.lblPlayerScore.setText('Your Score : {}'.format(palyerScore))
        elif (self.rdPc == 3) and (self.rdYou == 1):
            MsgBox = QMessageBox.information(self, 'Information', 'You Wins !!')
            palyerScore += 1
            self.lblPlayerScore.setText('Your Score : {}'.format(palyerScore))
        elif self.rdYou == 1 and self.rdPc == 2:
            MsgBox = QMessageBox.information(self, 'Information', 'You Lose !!')
            pcScore += 1
            self.lblComputerScore.setText('Computer Score : {}'.format(pcScore))
        elif self.rdYou == 2 and self.rdPc == 3:
            MsgBox = QMessageBox.information(self, 'Information', 'You Lose !!')
            pcScore += 1
            self.lblComputerScore.setText('Computer Score : {}'.format(pcScore))
        elif self.rdYou == 3 and self.rdPc == 1:
            MsgBox = QMessageBox.information(self, 'Information', 'You Lose !!')
            pcScore += 1
            self.lblComputerScore.setText('Computer Score : {}'.format(pcScore))
        self.lblAttempts.setText('Attempts : {}'.format(count_times))

    def changeImg(self):
        self.memory_used()
        imgIdx = rd(1, 3)
        imgCurrent = Paper
        if imgIdx == 1:
            imgCurrent = Paper
        elif imgIdx == 2:
            imgCurrent = Scissors
        elif imgIdx == 3:
            imgCurrent = Rook
        return imgCurrent

    @staticmethod
    def memory_used():
        pid = os.getpid()
        print(pid)
        ps = psutil.Process()
        # get memory use info
        memory_use = ps.memory_info()
        XXL = memoryview
        print('Memory Used :', memory_use)


def main():
    # create pyqt5 app
    App = QApplication(sys.argv)

    # create the instance of our Window
    window = Window()

    # start the app
    sys.exit(App.exec())


if __name__ == '__main__':
    main()
