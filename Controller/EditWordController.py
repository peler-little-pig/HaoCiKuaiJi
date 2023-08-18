from PyQt5.QtCore import QUrl, QModelIndex, Qt
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtWidgets import QMainWindow, QInputDialog, QTableWidget, QTableWidgetItem, QPushButton, QMessageBox, \
    QListWidgetItem, QFileDialog, QDialog

from DataStructure.Word import Word
from Model.EditWordModel import EditWordModel
from View.EditWordDialog import Ui_Dialog


class EditWordController(Ui_Dialog, QDialog):
    def __init__(self, word:Word, root=None):
        super().__init__(root)
        self.model = EditWordModel()
        self.word = word

        self.setupUi(self)
        self.show()
        self.event_connect()
        self.short_key_connect()

    def event_connect(self):
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

    def short_key_connect(self):
        ...

    def setupUi(self, Dialog):
        super().setupUi(Dialog)
        self.word_label.setText(self.word.word)
        self.part_of_speech_textEdit.setText(self.word.part_of_speech.replace(';;', '\n'))
        self.meaning_textEdit.setText(self.word.meaning.replace(';;', '\n'))
        self.example_textEdit.setText(self.word.example.replace(';;', '\n'))
        self.phonetic_symbol_textEdit.setText(self.word.phonetic_symbol.replace(';;', '\n'))
        self.audio_link_lineEdit.setText(self.word.audio_link)

    def accept(self) -> None:
        self.word.part_of_speech = self.part_of_speech_textEdit.toPlainText().replace('\n', ';;')
        self.word.meaning = self.meaning_textEdit.toPlainText().replace('\n', ';;')
        self.word.example = self.example_textEdit.toPlainText().replace('\n', ';;')
        self.word.phonetic_symbol = self.phonetic_symbol_textEdit.toPlainText().replace('\n', ';;')
        self.word.audio_link = self.audio_link_lineEdit.text()
        super().accept()
