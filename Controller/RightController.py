"""
Peler 2023
单词意思正确窗口
"""

from PyQt5.QtCore import pyqtSignal, QUrl, Qt
from PyQt5.QtGui import QKeySequence
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtWidgets import QMainWindow, QDialog, QShortcut

from Lib.AudioManager import AudioManager
from Model.RightModel import RightModel
from View.RightWindow import Ui_Dialog


class RightController(Ui_Dialog, QDialog):
    def __init__(self, word, dict, root=None):
        super().__init__(root)
        self.model = RightModel(dict)
        self.word = word
        # Create a media player instance
        self.media_player = QMediaPlayer()

        self.setupUi(self)
        self.show()
        self.event_connect()
        self.short_key_connect()

    def event_connect(self):
        self.init()
        self.right_pushButton.clicked.connect(self.right)
        self.wrong_pushButton.clicked.connect(self.wrong)
        self.play_pushButton.clicked.connect(lambda :AudioManager.play_radio(self.word))

    def short_key_connect(self):
        QShortcut(QKeySequence(Qt.Key_Space), self).activated.connect(self.wrong)
        QShortcut(QKeySequence(Qt.Key_Return), self).activated.connect(self.accept)
        QShortcut(QKeySequence(Qt.Key_P), self).activated.connect(lambda: AudioManager.play_radio(self.word))

    def init(self):
        # 隐藏关闭按钮
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)

        part_of_speech, chinese_definitions, example, phonetic_symbol = self.model.get_word_info(self.word)
        self.word_label.setText(self.word)
        self.part_label.setText(part_of_speech.replace(';;', ' '))
        self.meaning_label.setText(chinese_definitions.replace(';;', '\n'))
        self.example_label.setText(example.replace(';;', '\n'))
        self.play_pushButton.setText(f'播放音频 {phonetic_symbol}')
        AudioManager.play_radio(self.word)

    def right(self):
        self.accept()

    def wrong(self):
        self.reject()

    def play_word(self):
        audio = QMediaContent(QUrl(self.model.get_audio_link(self.word)))
        self.media_player.setMedia(audio)
        self.media_player.play()

    def keyPressEvent(self, event):
        # 禁用默认键盘检测，什么也不做
        pass