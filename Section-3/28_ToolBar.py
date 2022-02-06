import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt


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
        # K-ToolBar
        tb = self.addToolBar('My ToolBar')
        tb.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        new_tb = QAction(QIcon('../images/folder-1439.png'), 'New', self)
        add_tb = QAction(QIcon('../images/fileP.png'), 'Add', self)
        open_tb = QAction(QIcon('../images/openicon.png'), 'Open', self)
        self.lblnew = QLabel('Hello Kamal', self)
        self.lblnew.move(200, 200)
        tb.addAction(new_tb)
        tb.addAction(add_tb)
        tb.addAction(open_tb)
        new_tb.triggered.connect(self.new_tb_click)
        tb.actionTriggered.connect(self.btnfun)
        self.combo = QComboBox()
        self.combo.addItems(['Hi One', 'Hello Two', 'Good night Three'])
        tb.addWidget(self.combo)

        self.show()

    def new_tb_click(self):
        self.lblnew.setText('new tb is clicked')

    def btnfun(self, btn):
        if btn.text() == 'Open':
            self.lblnew.setText('Open tb is clicked')
        elif btn.text() == 'Add':
            self.lblnew.setText('Add tb is clicked')

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
