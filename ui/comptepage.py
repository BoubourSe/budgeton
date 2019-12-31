from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Slot

from ui.ui_comptepage import Ui_ComptePage


class ComptePage(QWidget):

    def __init__(self):
        super(ComptePage, self).__init__()
        self.ui = Ui_ComptePage()
        self.ui.setupUi(self)     