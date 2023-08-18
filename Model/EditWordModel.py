import csv
import json
import os
import shutil

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QProgressDialog

from DataStructure.WordList import WordList
from Lib.WordSearcher import WordSearcher
from SharedData.DictionaryData import DictionaryData


class EditWordModel(object):
    def __init__(self):
        ...