# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Z:\_Dev\Python\Budgeton\qt_ui\mainwindow.ui',
# licensing of 'Z:\_Dev\Python\Budgeton\qt_ui\mainwindow.ui' applies.
#
# Created: Tue Dec 31 17:10:37 2019
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.topButtonLayout = QtWidgets.QHBoxLayout()
        self.topButtonLayout.setObjectName("topButtonLayout")
        self.buttonCompte = QtWidgets.QPushButton(self.centralwidget)
        self.buttonCompte.setObjectName("buttonCompte")
        self.topButtonLayout.addWidget(self.buttonCompte)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.topButtonLayout.addItem(spacerItem)
        self.buttonBudget = QtWidgets.QPushButton(self.centralwidget)
        self.buttonBudget.setObjectName("buttonBudget")
        self.topButtonLayout.addWidget(self.buttonBudget)
        self.buttonCategorie = QtWidgets.QPushButton(self.centralwidget)
        self.buttonCategorie.setObjectName("buttonCategorie")
        self.topButtonLayout.addWidget(self.buttonCategorie)
        self.ButtonUser = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonUser.setObjectName("ButtonUser")
        self.topButtonLayout.addWidget(self.ButtonUser)
        self.verticalLayout.addLayout(self.topButtonLayout)
        self.stack = QtWidgets.QStackedWidget(self.centralwidget)
        self.stack.setObjectName("stack")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.stack.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.stack.addWidget(self.page_4)
        self.verticalLayout.addWidget(self.stack)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFichier = QtWidgets.QMenu(self.menubar)
        self.menuFichier.setObjectName("menuFichier")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionSettings = QtWidgets.QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.actionOuvrir = QtWidgets.QAction(MainWindow)
        self.actionOuvrir.setObjectName("actionOuvrir")
        self.menuFichier.addAction(self.actionOuvrir)
        self.menuFichier.addAction(self.actionSettings)
        self.menuFichier.addSeparator()
        self.menuFichier.addAction(self.actionClose)
        self.menubar.addAction(self.menuFichier.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.buttonCompte.setText(QtWidgets.QApplication.translate("MainWindow", "Compte", None, -1))
        self.buttonBudget.setText(QtWidgets.QApplication.translate("MainWindow", "Budget", None, -1))
        self.buttonCategorie.setText(QtWidgets.QApplication.translate("MainWindow", "Categories", None, -1))
        self.ButtonUser.setText(QtWidgets.QApplication.translate("MainWindow", "Utilisateurs", None, -1))
        self.menuFichier.setTitle(QtWidgets.QApplication.translate("MainWindow", "Fichier", None, -1))
        self.actionClose.setText(QtWidgets.QApplication.translate("MainWindow", "Quitter", None, -1))
        self.actionClose.setToolTip(QtWidgets.QApplication.translate("MainWindow", "<html><head/><body><p>Fermer l\'application</p></body></html>", None, -1))
        self.actionClose.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+Q", None, -1))
        self.actionSettings.setText(QtWidgets.QApplication.translate("MainWindow", "Settings", None, -1))
        self.actionOuvrir.setText(QtWidgets.QApplication.translate("MainWindow", "Ouvrir", None, -1))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

