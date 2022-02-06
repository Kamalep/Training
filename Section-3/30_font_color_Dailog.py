import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Font Color Dialog')
        self.setGeometry(350, 150, 400, 400)  # x, y, width, high
        self.UI()

    def UI(self):
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        self.editor = QTextEdit()
        self.editor.setText('You can write any thing and use buttons blow to change font and color')
        btnfile = QPushButton('Open File')
        btnfile.clicked.connect(self.openfile)
        btnfont = QPushButton('Change Font')
        btnfont.clicked.connect(self.fontchange)
        btncolor = QPushButton('Change Color')
        btncolor.clicked.connect(self.colorchange)
        vbox.addWidget(self.editor)
        vbox.addLayout(hbox)
        hbox.addStretch()
        hbox.addWidget(btnfile)
        hbox.addWidget(btnfont)
        hbox.addWidget(btncolor)
        hbox.addStretch()
        self.setLayout(vbox)

        self.show()

    def fontchange(self):
        font, ok = QFontDialog.getFont()
        print(font)
        print(ok)
        if ok:
            self.editor.setCurrentFont(font)

    def colorchange(self):
        color = QColorDialog.getColor()
        self.editor.setTextColor(color)

    def openfile(self):
        url = QFileDialog.getOpenFileName(self, 'Open a File', '', 'All Kamal file (*);;JPEG Format (*.jpg; '
                                                                   '*.jpeg);;Madia Format (*.mp3; *.mp4);;Text (*.txt)')
        file_url = url[0]
        print(url)
        print(file_url)
        file = open(file_url, 'r')
        content = file.read()
        file.close()
        self.editor.setText(content)


def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
