from PySide2.QtWidgets import QMainWindow, QFileDialog
from PySide2.QtCore import QFile, Slot, SIGNAL, SLOT, QObject
from pathlib import Path

from PySide2.QtWidgets import QShortcut

# Ui
from ui.ui_mainwindow import Ui_MainWindow
from ui.comptepage import ComptePage


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # slot button
        self.ui.buttonCompte.clicked.connect(self.on_click_button_compte)
        QObject.connect(self.ui.actionClose, SIGNAL("triggered()"), self, SLOT('on_click_menu_button_close()'))
        QObject.connect(self.ui.actionOuvrir, SIGNAL("triggered()"), self, SLOT('on_click_menu_button_open()'))

        # widget
        self.comptepage = ComptePage()
        self.ui.stack.addWidget(self.comptepage)

        #default page
        self.ui.stack.setCurrentWidget(self.comptepage)

    @Slot()
    def on_click_button_compte(self):
        self.ui.stack.setCurrentWidget(self.comptepage)

    @Slot()
    def on_click_menu_button_close(self):
        self.close()

    @Slot()
    def on_click_menu_button_open(self):
        """Open database file"""
        w = QFileDialog(self, directory=str(Path.home().absolute()), caption="Selectionnez la base de donné", filter="Base de donnée SQLite (*.sqlite)")
        w.open()

