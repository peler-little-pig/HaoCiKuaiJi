from PyQt5.QtWidgets import QDialog

from Model.HelpTechModel import HelpTechModel
from View.HelpTechDialog import Ui_Dialog


class HelpTechController(Ui_Dialog, QDialog):
    def __init__(self, root=None):
        super().__init__(root)
        self.model = HelpTechModel()

        self.setupUi(self)
        self.show()