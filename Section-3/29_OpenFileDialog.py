import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Open File Dialog')
        self.setGeometry(350, 150, 400, 400)  # x, y, width, high
        self.user_interface()

    def user_interface(self):
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        self.editor = QTextEdit()
        btnfile = QPushButton('Open File')
        btnfile.clicked.connect(self.openfile)
        vbox.addWidget(self.editor)
        vbox.addLayout(hbox)
        hbox.addStretch()
        hbox.addWidget(btnfile)
        hbox.addStretch()
        self.setLayout(vbox)

        self.show()

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
