"""
Peler 2023
单词意思检测窗口
"""

from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QKeySequence
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtWidgets import QMainWindow, QListWidgetItem, QInputDialog, QListWidget, QDialog, QMessageBox, QShortcut

from Controller.RightController import RightController
from Controller.WrongController import WrongController
from Model.StudySpellModel import SpellModel
from View.StudySpellWindow import Ui_MainWindow


class SpellController(Ui_MainWindow, QMainWindow):
    def __init__(self, group, root=None):
        super().__init__(root)
        self.model = SpellModel(group)
        # Create a media player instance
        self.media_player = QMediaPlayer()

        self.next_word = ""

        self.setupUi(self)
        self.show()
        self.event_connect()
        self.short_key_connect()

    def event_connect(self):
        self.init()
        self.ensure_pushButton.clicked.connect(self.check)

    def short_key_connect(self):
        QShortcut(QKeySequence(Qt.Key_Return), self).activated.connect(self.check)
        QShortcut(QKeySequence(Qt.Key_P), self).activated.connect(lambda: self.play_word(self.word_label.text()))

    def init(self):
        self.next()
        self.test_lineEdit.setFocus()

    def next(self):
        self.next_word = self.model.get_next_word()
        if self.next_word is not None:
            self.word_label.setText(self.model.get_chinese_definitions(self.next_word))
            self.play_word(self.next_word)
            self.play_pushButton.setText(f'播放音频{self.model.get_phonetic_symbol(self.next_word)}')
            self.play_pushButton.clicked.connect(lambda: self.play_word(self.next_word))
            self.test_lineEdit.clear()
        else:
            QMessageBox.information(self, "信息", "您已经将单词背完了，记得常来复习哦")

    def check(self):
        if self.test_lineEdit.text() == self.next_word:
            self.right()
        else:
            self.wrong()

    def right(self):
        window = RightController(self.next_word, self.model.dict)
        result = window.exec_()
        if result == QDialog.Accepted:
            self.model.right(self.next_word)
            self.next()
        else:
            self.model.wrong(self.next_word)
            self.next()

    def wrong(self):
        window = WrongController(self.next_word, self.model.dict)
        result = window.exec_()
        if result == QDialog.Accepted:
            self.model.wrong(self.next_word)
            self.next()

    def play_word(self, word):
        # Load the MP3 file
        media_content = QMediaContent(QUrl.fromLocalFile(f'./res/{word}.mp3'))
        self.media_player.setMedia(media_content)

        # Play the MP3
        self.media_player.play()

    def keyPressEvent(self, event):
        # 禁用默认键盘检测，什么也不做
        pass
