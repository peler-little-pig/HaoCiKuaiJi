from PyQt5.QtWidgets import QDialog

from Model.SupportModel import SupportModel
from View.SupportDialog import Ui_Dialog


class SupportController(Ui_Dialog, QDialog):
    def __init__(self, root=None):
        super().__init__(root)
        self.model = SupportModel()

        self.setupUi(self)
        self.show()