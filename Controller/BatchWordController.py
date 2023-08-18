from PyQt5.QtCore import QUrl, QModelIndex, Qt
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtWidgets import QMainWindow, QInputDialog, QTableWidget, QTableWidgetItem, QPushButton, QMessageBox, \
    QListWidgetItem, QFileDialog, QDialog
from Model.BatchWordModel import BatchWordModel
from SharedData.DictionaryData import DictionaryData
from View.BatchWordDialog import Ui_Dialog


class BatchWordController(Ui_Dialog, QDialog):
    def __init__(self, root=None):
        super().__init__(root)
        self.model = BatchWordModel()

        self.setupUi(self)
        self.show()
        self.event_connect()
        self.short_key_connect()

    def event_connect(self):
        self.add_pushButton.clicked.connect(self.new_word)
        self.delete_pushButton.clicked.connect(self.delete_word)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

    def short_key_connect(self):
        ...

    def new_word(self):
        text, ok = QInputDialog.getText(self, '添加单词', '请输入要添加的单词')
        if ok:
            if not self.model.is_exist_word(text):
                self.model.new_word(text)
                self.update_word()
            else:
                QMessageBox.information(self, "提示", f"单词{text}重复", QMessageBox.Ok, QMessageBox.Ok)


    def delete_word(self):
        selected_items = self.listWidget.selectedItems()
        if selected_items:
            for item in selected_items:
                self.model.delete_word(item.text())
        self.update_word()

    def update_word(self):
        self.listWidget.clear()
        self.listWidget.addItems(self.model.word_list)