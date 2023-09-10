from PyQt5.QtCore import QUrl, QModelIndex, Qt
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtWidgets import QMainWindow, QInputDialog, QTableWidget, QTableWidgetItem, QPushButton, QMessageBox, \
    QListWidgetItem, QFileDialog, QDialog

from DataStructure.Word import Word
from Lib.Settings import Settings
from Model.SettingModel import SettingModel
from View.SettingDialog import Ui_Dialog


class SettingController(Ui_Dialog, QDialog):
    def __init__(self, root=None):
        super().__init__(root)
        self.model = SettingModel()

        self.setupUi(self)
        self.show()
        self.event_connect()
        self.short_key_connect()

    def event_connect(self):
        self.init()
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

    def short_key_connect(self):
        ...

    def init(self):
        self.audio_download_no_radioButton.setChecked(Settings.settings['audio_download_no'])
        self.audio_download_group_radioButton.setChecked(Settings.settings['audio_download_group'])
        self.audio_download_study_radioButton.setChecked(Settings.settings['audio_download_study'])
        self.audio_download_save_network_checkBox.setChecked(Settings.settings['audio_download_save_network'])
        self.group_allow_multselect_checkBox.setChecked(Settings.settings['group_allow_multselect'])
        self.group_ask_delete_checkBox.setChecked(Settings.settings['group_ask_delete'])
        self.group_auto_order_radioButton.setChecked(Settings.settings['group_auto_order'])
        self.group_reserve_auto_order_radioButton.setChecked(Settings.settings['group_reserve_auto_order'])
        self.word_allow_multselect_checkBox.setChecked(Settings.settings['word_allow_multselect'])
        self.word_ask_delete_checkBox.setChecked(Settings.settings['word_ask_delete'])
        self.word_auto_order_radioButton.setChecked(Settings.settings['word_auto_order'])
        self.word_reserve_auto_order_radioButton.setChecked(Settings.settings['word_reserve_auto_order'])

    def accept(self) -> None:
        Settings.settings['audio_download_no'] = self.audio_download_no_radioButton.isChecked()
        Settings.settings['audio_download_group'] = self.audio_download_group_radioButton.isChecked()
        Settings.settings['audio_download_study'] = self.audio_download_study_radioButton.isChecked()
        Settings.settings['audio_download_save_network'] = self.audio_download_save_network_checkBox.isChecked()
        Settings.settings['group_allow_multselect'] = self.group_allow_multselect_checkBox.isChecked()
        Settings.settings['group_ask_delete'] = self.group_ask_delete_checkBox.isChecked()
        Settings.settings['group_auto_order'] = self.group_auto_order_radioButton.isChecked()
        Settings.settings['group_reserve_auto_order'] = self.group_reserve_auto_order_radioButton.isChecked()
        Settings.settings['word_allow_multselect'] = self.word_allow_multselect_checkBox.isChecked()
        Settings.settings['word_ask_delete'] = self.word_ask_delete_checkBox.isChecked()
        Settings.settings['word_auto_order'] = self.word_auto_order_radioButton.isChecked()
        Settings.settings['word_reserve_auto_order'] = self.word_reserve_auto_order_radioButton.isChecked()
        super().accept()
