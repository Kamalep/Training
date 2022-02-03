import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Menu Widget')
        self.setGeometry(350, 150, 600, 600)  # x, y, width, high
        self.user_interface()

    def user_interface(self):
        # K-main_menu
        menu_bar = self.menuBar()
        file = menu_bar.addMenu('File')
        edit = menu_bar.addMenu('Edit')
        code = menu_bar.addMenu('Code')
        help_menu = menu_bar.addMenu('Help')

        # K-Sub_main_menu
        new = QAction('New Project', self)
        new.setShortcut('Ctrl+N')
        file.addAction(new)

        open_ = QAction('Open', self)
        open_.setShortcut('Ctrl+O')
        file.addAction(open_)

        exit_ = QAction('Exit', self)
        exit_.setShortcut('Ctrl+X')
        exit_.setIcon(QIcon('../images/exit-icon-16x16-17.jpg'))
        exit_.triggered.connect(self.exit_click)
        file.addAction(exit_)

        self.show()

    def exit_click(self):
        msgbox = QMessageBox.information(self, 'Warning', 'Are you sure to exit?', QMessageBox.Yes | QMessageBox.No,
                                         QMessageBox.No)
        if msgbox == QMessageBox.Yes:
            sys.exit()


def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
