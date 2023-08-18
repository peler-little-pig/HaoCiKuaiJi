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
from Model.StudyMeaningModel import TestModel
from View.StudyMeaningWindow import Ui_MainWindow


class TestController(Ui_MainWindow, QMainWindow):
    def __init__(self, group, root=None):
        super().__init__(root)
        self.model = TestModel(group)
        # Create a media player instance
        self.media_player = QMediaPlayer()

        self.setupUi(self)
        self.show()
        self.event_connect()
        self.short_key_connect()

    def event_connect(self):
        self.init()
        self.tip_pushButton.clicked.connect(self.show_tip)
        self.yes_pushButton.clicked.connect(self.right)
        self.no_pushButton.clicked.connect(self.wrong)

    def short_key_connect(self):
        QShortcut(QKeySequence(Qt.Key_Return), self).activated.connect(self.right)
        QShortcut(QKeySequence(Qt.Key_Space), self).activated.connect(self.wrong)
        QShortcut(QKeySequence(Qt.Key_H), self).activated.connect(self.show_tip)
        QShortcut(QKeySequence(Qt.Key_P), self).activated.connect(lambda: self.play_word(self.word_label.text()))

    def init(self):
        self.next()

    def show_tip(self):
        self.tip_label.setText(self.model.get_tips(self.word_label.text()))

    def next(self):
        next_word = self.model.get_next_word()
        if next_word is not None:
            self.word_label.setText(next_word)
            self.tip_label.setText('')
            self.play_word(next_word)
            self.play_pushButton.setText(f'播放音频{self.model.get_phonetic_symbol(next_word)}')
            self.play_pushButton.clicked.connect(lambda: self.play_word(next_word))
        else:
            QMessageBox.information(self, "信息", "您已经将单词背完了，记得常来复习哦")

    def right(self):
        window = RightController(self.word_label.text(), self.model.dict)
        result = window.exec_()
        if result == QDialog.Accepted:
            self.model.right(self.word_label.text())
            self.next()
        else:
            self.model.wrong(self.word_label.text())
            self.next()

    def wrong(self):
        window = WrongController(self.word_label.text(), self.model.dict)
        result = window.exec_()
        if result == QDialog.Accepted:
            self.model.wrong(self.word_label.text())
            self.next()

    def play_word(self, word):
        audio = QMediaContent(QUrl(self.model.get_audio_link(word)))
        self.media_player.setMedia(audio)
        self.media_player.play()

    def keyPressEvent(self, event):
        # 禁用默认键盘检测，什么也不做
        pass
