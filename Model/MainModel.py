import csv
import json
import os
import shutil

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QProgressDialog

from DataStructure.Word import Word
from DataStructure.WordList import WordList
from Lib.AudioManager import AudioManager
from Lib.ExportData import ExportData
from Lib.Settings import Settings
from Lib.WordSearcher import WordSearcher
from SharedData.DictionaryData import DictionaryData


class MainModel(object):
    def __init__(self):
        self.group_list = []

    def init_group(self):
        for file in os.listdir('./AppData/dictionary'):
            self.group_list.append(file)

    def new_group(self, name):
        path = f'./AppData/dictionary/{name}'
        os.mkdir(path)
        with open(f'{path}/words.csv', 'w', encoding='utf-8'):
            ...
        self.group_list.append(name)

    def delete_group(self, name):
        shutil.rmtree(f'./AppData/dictionary/{name}')
        self.group_list.remove(name)

    def rename_group(self, old_name, new_name):
        os.rename(f'./AppData/dictionary/{old_name}', f'./AppData/dictionary/{new_name}')
        index = self.group_list.index(old_name)
        self.group_list[index] = new_name

    def import_group(self, path):
        name = os.path.basename(path)
        if name in self.group_list:
            name += "(导入)"
        shutil.copytree(path, f'./AppData/dictionary/{name}')
        self.group_list.append(name)

    def import_old_group(self, path):
        with open(f'{path}/words.json', 'r') as file:
            word_info_list = [json.loads(line) for line in file]
            print(word_info_list)
        name = os.path.basename(path)
        if name in self.group_list:
            name += "(导入)"
        self.new_group(name)
        with open(f'./AppData/dictionary/{name}/words.csv', 'w', encoding='utf-8', newline="") as f:
            csv_writer = csv.writer(f)
            header = ["word", "part_of_speech", "meaning", "example", "phonetic_symbol", "audio_link"]
            csv_writer.writerow(header)

            progressDialog = QProgressDialog("正在导入旧版单词组", "取消", 0, len(word_info_list), None)
            progressDialog.setWindowTitle('请稍后')
            progressDialog.show()
            is_break = False
            for i in range(len(word_info_list)):
                csv_writer.writerow(
                    [word_info_list[i]['word'], word_info_list[i]['part_of_speech'],
                     word_info_list[i]['chinese_definitions_list'], word_info_list[i]['example'],
                     word_info_list[i]['phonetic_symbol'], WordSearcher.search_audio_link(word_info_list[i]['word'])])
                QCoreApplication.processEvents()
                progressDialog.setValue(i)
                if progressDialog.wasCanceled():
                    is_break = True
                    break
        if is_break:
            self.delete_group(name)
        progressDialog.setValue(len(word_info_list))

    def export_group(self, name, target):
        shutil.copytree(f'./AppData/dictionary/{name}', target)

    def update_data_group(self):
        progressDialog = QProgressDialog("正在更新单词组", "取消", 0, len(DictionaryData.current_word_list), None)
        progressDialog.setWindowTitle('请稍后')
        progressDialog.show()
        for i in range(len(DictionaryData.current_word_list)):
            DictionaryData.current_word_list[i] = WordSearcher.search_all(DictionaryData.current_word_list[i].word)
            QCoreApplication.processEvents()
            progressDialog.setValue(i)
            if progressDialog.wasCanceled():
                break

    def download_group(self):
        AudioManager.download_audio()

    def save_network_clean_group(self):
        AudioManager.save_network_clean_audio()

    def save_network_download_group(self, group_weight):
        group_list = []
        for i in range(group_weight.count()):
            wl = WordList(group_weight.item(i).text())
            wl.load_word(f'./AppData/dictionary/{group_weight.item(i).text()}/words.csv')
            group_list.append(wl)
        AudioManager.save_network_download_audio(group_list)

    def save_network_check_group(self, group_weight):
        group_list = []
        for i in range(group_weight.count()):
            wl = WordList(group_weight.item(i).text())
            wl.load_word(f'./AppData/dictionary/{group_weight.item(i).text()}/words.csv')
            group_list.append(wl)
        return AudioManager.save_network_check_audio(group_list)

    def load_word(self, group):
        DictionaryData.current_word_list = WordList(group)
        DictionaryData.current_word_list.load_word(f'./AppData/dictionary/{group}/words.csv')
        if Settings.settings['audio_download_group']:
            AudioManager.download_audio()

    def add_auto_word(self, word):
        DictionaryData.current_word_list.append(WordSearcher.search_all(word))

    def add_inauto_word(self, word_):
        word = Word(word_, "未定义", "未定义", "未定义", "未定义", "未定义")
        DictionaryData.current_word_list.append(word)

    def delete_word(self, word):
        DictionaryData.current_word_list.remove(word)

    def edit_word(self, word) -> Word:
        return DictionaryData.current_word_list.get_word(word)

    def is_exist_word(self, word):
        return DictionaryData.current_word_list.get_word(word) is not None

    def save_word(self):
        if DictionaryData.current_word_list:
            DictionaryData.current_word_list.save_word()

    def init_study(self):
        if Settings.settings['audio_download_study']:
            AudioManager.download_audio()

    def pure_table_csv_export(self, path):
        ExportData.export_pure_table_csv(path)
