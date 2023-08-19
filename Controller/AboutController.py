from PyQt5.QtWidgets import QDialog

from Model.AboutModel import AboutModel
from View.AboutDialog import Ui_Dialog


class AboutController(Ui_Dialog, QDialog):
    def __init__(self, root=None):
        super().__init__(root)
        self.model = AboutModel()

        self.setupUi(self)
        self.show()