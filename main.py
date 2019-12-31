# This Python file uses the following encoding: utf-8
import sys
from PySide2 import QtGui, QtCore, QtWidgets
from PySide2.QtWidgets import QApplication
from ui.mainwindow import MainWindow
from conf import Conf




if __name__ == "__main__":

    app = QApplication(sys.argv)

    win = MainWindow()
    win.show()

    sys.exit(app.exec_())
