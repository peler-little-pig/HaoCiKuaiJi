"""
Peler 2023
单词意思错误窗口
"""

from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtGui import QKeySequence
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtWidgets import QMainWindow, QDialog, QShortcut

from Model.WrongModel import WrongModel
from View.WrongWindow import Ui_Dialog


class WrongController(Ui_Dialog, QDialog):
    def __init__(self, word, dict, root=None):
        super().__init__(root)
        self.model = WrongModel(dict)
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
        self.play_pushButton.clicked.connect(self.play_word)

    def short_key_connect(self):
        QShortcut(QKeySequence(Qt.Key_Return), self).activated.connect(self.right)
        QShortcut(QKeySequence(Qt.Key_P), self).activated.connect(lambda: self.play_word())

    def init(self):
        # 隐藏关闭按钮
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)

        part_of_speech, chinese_definitions, example, phonetic_symbol = self.model.get_word_info(self.word)
        self.word_label.setText(self.word)
        self.part_label.setText(part_of_speech.replace(';;', ' '))
        self.meaning_label.setText(chinese_definitions.replace(';;', '\n'))
        self.example_label.setText(example.replace(';;', '\n'))
        self.play_pushButton.setText(f'播放音频 {phonetic_symbol}')
        self.play_word()

    def right(self):
        self.accept()

    def play_word(self):
        audio = QMediaContent(QUrl(self.model.get_audio_link(self.word)))
        self.media_player.setMedia(audio)
        self.media_player.play()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:  # 处理回车键事件
            self.right()
        else:
            self.play_word()

    def keyPressEvent(self, event):
        # 禁用默认键盘检测，什么也不做
        pass
