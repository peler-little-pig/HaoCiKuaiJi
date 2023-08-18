import csv
import json
import os
import shutil

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QProgressDialog

from DataStructure.WordList import WordList
from Lib.WordSearcher import WordSearcher
from SharedData.DictionaryData import DictionaryData


class BatchWordModel(object):
    def __init__(self):
        self.word_list = []

    def new_word(self, name):
        self.word_list.append(name)

    def delete_word(self, name):
        self.word_list.remove(name)

    def is_exist_word(self, word_):
        for word in self.word_list:
            if word == word_:
                return True
        return False or DictionaryData.current_word_list.get_word(word_) is not None
