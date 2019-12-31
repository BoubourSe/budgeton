# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\comptewidget.ui',
# licensing of 'ui\comptewidget.ui' applies.
#
# Created: Thu Dec 12 21:39:02 2019
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_ComptePage(object):
    def setupUi(self, CompteWidget):
        CompteWidget.setObjectName("CompteWidget")
        CompteWidget.resize(842, 518)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(CompteWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(CompteWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(CompteWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableView = QtWidgets.QTableView(CompteWidget)
        self.tableView.setObjectName("tableView")
        self.verticalLayout.addWidget(self.tableView)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(CompteWidget)
        QtCore.QMetaObject.connectSlotsByName(CompteWidget)

    def retranslateUi(self, CompteWidget):
        CompteWidget.setWindowTitle(QtWidgets.QApplication.translate("CompteWidget", "Form", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("CompteWidget", "Compte", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("CompteWidget", "@TODO: Filtres", None, -1))

