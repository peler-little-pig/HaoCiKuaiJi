import os
import shutil

import requests
from PyQt5.QtCore import QCoreApplication, QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtWidgets import QProgressDialog

from Lib.Settings import Settings
from Lib.WordSearcher import WordSearcher
from SharedData.DictionaryData import DictionaryData
from SharedData.StateData import StateData


class AudioManager(staticmethod):
    media_player = QMediaPlayer()
    @staticmethod
    def save_audio(word):
        # 设置请求头，模拟浏览器访问
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
        }
        response = requests.get(WordSearcher.search_audio_link(word), headers=headers)
        if response.status_code == 200:
            with open(f'./AppData/temp/{word}.mp3', 'wb') as f:
                f.write(response.content)

    @staticmethod
    def download_audio():
        AudioManager.remove_audio()
        progressDialog = QProgressDialog("正在缓存单词音频", "取消", 0, len(DictionaryData.current_word_list), None)
        progressDialog.setWindowTitle('请稍后')
        progressDialog.show()
        is_break = False
        for i in range(len(DictionaryData.current_word_list)):
            AudioManager.save_audio(DictionaryData.current_word_list[i].word)
            QCoreApplication.processEvents()
            progressDialog.setValue(i)
            if progressDialog.wasCanceled():
                is_break = True
                break
        if is_break:
            AudioManager.remove_audio()
        else:
            StateData.is_audio_download = True
        progressDialog.setValue(len(DictionaryData.current_word_list))

    @staticmethod
    def remove_audio():
        shutil.rmtree('./AppData/temp')
        os.mkdir('./AppData/temp')
        StateData.is_audio_download = False

    @staticmethod
    def play_radio(word):
        if StateData.is_audio_download:
            audio = QMediaContent(QUrl.fromLocalFile(f'./AppData/temp/{word}.mp3'))
        else:
            audio = QMediaContent(QUrl(WordSearcher.search_audio_link(word)))
        AudioManager.media_player.setMedia(audio)
        AudioManager.media_player.play()
