import shutil
import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import QUrl, QModelIndex, Qt, QCoreApplication
from PyQt5.QtGui import QKeySequence
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtWidgets import QMainWindow, QInputDialog, QTableWidget, QTableWidgetItem, QPushButton, QMessageBox, \
    QListWidgetItem, QFileDialog, QProgressDialog, QShortcut, QAbstractItemView

from Controller.AboutController import AboutController
from Controller.BatchWordController import BatchWordController
from Controller.EditWordController import EditWordController
from Controller.HelpTechController import HelpTechController
from Controller.SettingController import SettingController
from Controller.StudyMeaningController import StudyMeaningController
from Controller.StudySpellController import StudySpellController
from Controller.SupportController import SupportController
from Lib.AudioManager import AudioManager
from Lib.Settings import Settings
from Model.MainModel import MainModel
from SharedData.AppData import AppData
from SharedData.DictionaryData import DictionaryData
from View import EditWordDialog
from View.MainWindow import Ui_MainWindow
from multiprocessing import Process


class MainController(Ui_MainWindow, QMainWindow):
    def __init__(self, root=None):
        super().__init__(root)
        self.model = MainModel()

        self.setupUi(self)
        self.show()
        self.event_connect()
        self.short_key_connect()

    def event_connect(self):
        self.init()
        self.group_new_action.triggered.connect(self.new_group)
        self.group_delect_action.triggered.connect(self.delete_group)
        self.group_rename_action.triggered.connect(self.rename_group)
        self.group_import_action.triggered.connect(self.import_group)
        self.group_export_action.triggered.connect(self.export_group)
        self.group_import_old_action.triggered.connect(self.import_old_group)
        self.group_lineEdit.textChanged.connect(self.search_group)
        self.group_listWidget.doubleClicked.connect(self.load_word)
        self.group_update_data_action.triggered.connect(self.update_data_group)
        self.word_add_auto_word_action.triggered.connect(self.add_auto_word)
        self.word_add_inauto_word_action.triggered.connect(self.add_inauto_word)
        self.word_add_batch_action.triggered.connect(self.add_batch_word)
        self.word_delect_action.triggered.connect(self.delete_word)
        self.word_edit_action.triggered.connect(self.edit_word)
        self.word_tableWidget.doubleClicked.connect(self.edit_word)
        self.word_lineEdit.textChanged.connect(self.search_word)
        self.study_meaning_action.triggered.connect(self.show_meaning_study)
        self.study_spell_action.triggered.connect(self.show_spell_study)
        self.setting_dialog_action.triggered.connect(self.show_dialog_setting)
        self.setting_export_action.triggered.connect(self.export_setting)
        self.setting_import_action.triggered.connect(self.import_setting)
        self.export_pure_table_csv_action.triggered.connect(self.pure_table_csv_export)
        self.export_pure_table_excel_action.triggered.connect(self.pure_table_excel_export)
        self.export_meaning_word_action.triggered.connect(self.meaning_word_export)
        self.export_meaning_pdf_action.triggered.connect(self.meaning_pdf_export)
        self.export_spell_word_action.triggered.connect(self.spell_word_export)
        self.export_spell_pdf_action.triggered.connect(self.spell_pdf_export)
        self.help_about_action.triggered.connect(self.show_about_dialog_help)
        self.help_support_action.triggered.connect(self.show_support_dialog_help)
        self.help_tech_support_action.triggered.connect(self.show_help_tech_dialog_help)

    def init(self):
        # 设置表格不可编辑
        self.word_tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)
        # 默认单选
        self.word_tableWidget.setSelectionMode(QTableWidget.SingleSelection)

        self.init_group()
        self.init_setting()

    def short_key_connect(self):
        QShortcut(QKeySequence(Qt.Key_A), self).activated.connect(self.add_auto_word)

    ###################################
    # GROUP ###########################
    ###################################
    def init_group(self):
        self.model.init_group()
        self.update_group()

    def new_group(self):
        text, ok = QInputDialog.getText(self, '创建单词组', '请输入单词组的名称')
        if ok:
            self.model.new_group(text)
            self.update_group()

    def delete_group(self):
        if Settings.settings['group_ask_delete']:
            msg_box = QMessageBox.question(self, "确认", "是否删除？", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            if msg_box == QMessageBox.Yes:
                ...
            else:
                return None
        selected_items = self.group_listWidget.selectedItems()
        if selected_items:
            for item in selected_items:
                self.model.delete_group(item.text())
        self.inactive_word()
        self.update_group()

    def rename_group(self):
        selected_item = self.group_listWidget.currentItem()
        if selected_item:
            current_name = selected_item.text()
            text, ok = QInputDialog.getText(self, '重命名单词组', '请输入单词组的名称')
            if ok:
                self.model.rename_group(current_name, text)
                self.update_group()

    def import_group(self):
        path = QFileDialog.getExistingDirectory(self, '导入单词组')
        if path:
            self.model.import_group(path)
            self.update_group()

    def import_old_group(self):
        path = QFileDialog.getExistingDirectory(self, '导入旧版本单词组')
        if path:
            self.model.import_old_group(path)
            self.update_group()

    def export_group(self):
        selected_item = self.group_listWidget.currentItem()
        if selected_item:
            path, type_ = QFileDialog.getSaveFileName(self, '导出单词组', selected_item.text(), "好词快记单词组格式")
            if path:
                self.model.export_group(selected_item.text(), path)

    def search_group(self, text):
        items = self.group_listWidget.findItems(text, Qt.MatchContains)
        for row in range(self.group_listWidget.count()):
            item = self.group_listWidget.item(row)
            item.setHidden(item not in items)

    def update_data_group(self):
        self.model.update_data_group()
        self.update_group()

    def update_group(self):
        self.group_listWidget.clear()
        self.group_listWidget.addItems(self.model.group_list)

        if Settings.settings['group_auto_order']:
            self.group_listWidget.sortItems(Qt.AscendingOrder)
        elif Settings.settings['group_reserve_auto_order']:
            self.group_listWidget.sortItems(Qt.DescendingOrder)

    ###################################
    # WORD ###########################
    ###################################
    def load_word(self, modelindex: QModelIndex):
        self.model.save_word()
        self.model.load_word(self.group_listWidget.item(modelindex.row()).text())
        self.update_word()

    def add_auto_word(self):
        text, ok = QInputDialog.getText(self, '添加单词', '请输入要搜索的单词')
        if ok:
            if not self.model.edit_word(text):
                self.model.add_auto_word(text)
                self.update_word()
                self.word_tableWidget.setCurrentItem(
                    self.word_tableWidget.item(self.word_tableWidget.rowCount() - 1, 0))
            else:
                QMessageBox.information(self, "提示", f"单词{text}重复", QMessageBox.Ok, QMessageBox.Ok)

    def add_inauto_word(self):
        text, ok = QInputDialog.getText(self, '添加单词', '请输入要手动添加的单词')
        if ok:
            if not self.model.is_exist_word(text):
                self.model.add_inauto_word(text)
                self.update_word()
                self.word_tableWidget.setCurrentItem(
                    self.word_tableWidget.item(self.word_tableWidget.rowCount() - 1, 0))
            else:
                QMessageBox.information(self, "提示", f"单词{text}重复", QMessageBox.Ok, QMessageBox.Ok)

    def add_batch_word(self):
        word_window = BatchWordController(self)
        if word_window.exec_():
            progressDialog = QProgressDialog("正在批量添加单词", "取消", 0, len(word_window.model.word_list), None)
            progressDialog.setWindowTitle('请稍后')
            progressDialog.show()
            is_break = False
            for i in range(len(word_window.model.word_list)):
                self.model.add_auto_word(word_window.model.word_list[i])
                QCoreApplication.processEvents()
                progressDialog.setValue(i)
                if progressDialog.wasCanceled():
                    is_break = True
                    break
            progressDialog.setValue(len(word_window.model.word_list))
            if is_break:
                pass
            self.update_word()

    def delete_word(self):
        if Settings.settings['word_ask_delete']:
            msg_box = QMessageBox.question(self, "确认", "是否删除？", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            if msg_box == QMessageBox.Yes:
                ...
            else:
                return None
        selected_items = self.word_tableWidget.selectedItems()
        rows_to_delete = set()

        # 获取选中的行号
        for item in selected_items:
            rows_to_delete.add(item.row())
            self.model.delete_word(self.word_tableWidget.item(item.row(), 0).text())

        # 按逆序删除选中的行，以防行号变化导致删除错误
        for row in sorted(rows_to_delete, reverse=True):
            self.word_tableWidget.removeRow(row)

    def edit_word(self, *args):
        row = self.word_tableWidget.currentRow()
        if row != -1:
            word = self.model.edit_word(self.word_tableWidget.item(row, 0).text())
            edit_dialog = EditWordController(word, self)
            edit_dialog.exec_()
            self.update_word()
        else:
            QMessageBox.information(self, "提示", "请选择单词进行编辑", QMessageBox.Ok, QMessageBox.Ok)

    def search_word(self, text):
        for row in range(self.word_tableWidget.rowCount()):
            item = self.word_tableWidget.item(row, 0)  # 获取每行的第一个单元格
            if item is not None:
                t = item.text()
                matched = text.lower() in t.lower()
                self.word_tableWidget.setRowHidden(row, not matched)

    def update_word(self):
        self.word_tableWidget.setRowCount(0)
        self.word_tableWidget.clearContents()
        self.active_word()
        for word in DictionaryData.current_word_list:
            self.insert_word(*word.get_value())

        if Settings.settings['word_auto_order']:
            self.word_tableWidget.sortItems(Qt.AscendingOrder)
        elif Settings.settings['word_reserve_auto_order']:
            self.word_tableWidget.sortItems(Qt.DescendingOrder)

    def insert_word(self, word: str, part_of_speech: list, meaning: list, example: list, phonetic_symbol: str,
                    audio_link: str):
        row_count = self.word_tableWidget.rowCount()
        self.word_tableWidget.insertRow(row_count)

        word_item = QTableWidgetItem(word)
        parts_of_speech_list_item = QTableWidgetItem(part_of_speech)
        chinese_definitions_item = QTableWidgetItem(meaning)
        example_list_item = QTableWidgetItem(example)
        self.word_tableWidget.setItem(row_count, 0, word_item)
        self.word_tableWidget.setItem(row_count, 1, parts_of_speech_list_item)
        self.word_tableWidget.setItem(row_count, 2, chinese_definitions_item)
        self.word_tableWidget.setItem(row_count, 3, example_list_item)

        # 添加播放音频按钮
        play_button = QPushButton(f'播放音频 {phonetic_symbol}', self)
        play_button.clicked.connect(lambda: AudioManager.play_radio(word))
        self.word_tableWidget.setCellWidget(row_count, 4, play_button)

    def inactive_word(self):
        self.word_tableWidget.setRowCount(0)
        self.word_tableWidget.clearContents()
        self.word_add_menu.setEnabled(False)
        self.word_delect_action.setEnabled(False)
        self.word_update_action.setEnabled(False)
        self.word_edit_action.setEnabled(False)
        self.word_tableWidget.setEnabled(False)
        self.word_lineEdit.setEnabled(False)

    def active_word(self):
        self.word_add_menu.setEnabled(True)
        self.word_delect_action.setEnabled(True)
        self.word_update_action.setEnabled(True)
        self.word_edit_action.setEnabled(True)
        self.word_tableWidget.setEnabled(True)
        self.word_lineEdit.setEnabled(True)

    ###################################
    # STUDY ###########################
    ###################################

    def show_meaning_study(self):
        self.model.init_study()
        StudyMeaningController(DictionaryData.current_word_list.group_name, self)

    def show_spell_study(self):
        self.model.init_study()
        StudySpellController(DictionaryData.current_word_list.group_name, self)

    ###################################
    # Other ###########################
    ###################################
    def closeEvent(self, a0):
        super().closeEvent(a0)
        self.model.save_word()
        AudioManager.remove_audio()
        Settings.save_data()

    ###################################
    # Setting #########################
    ###################################
    def show_dialog_setting(self):
        dialog = SettingController(self)
        dialog.exec_()
        self.init_setting()

    def init_setting(self):
        if Settings.settings['group_allow_multselect']:
            self.group_listWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        else:
            self.group_listWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        if Settings.settings['word_allow_multselect']:
            self.word_tableWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        else:
            self.word_tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        if Settings.settings['word_auto_order']:
            self.word_tableWidget.sortItems(Qt.AscendingOrder)
        elif Settings.settings['word_reserve_auto_order']:
            self.word_tableWidget.sortItems(Qt.DescendingOrder)
        if Settings.settings['group_auto_order']:
            self.group_listWidget.sortItems(Qt.AscendingOrder)
        elif Settings.settings['group_reserve_auto_order']:
            self.group_listWidget.sortItems(Qt.DescendingOrder)

    def import_setting(self):
        QMessageBox.information(self, "即将推出！", f"即将在v2.0.1版本推出此功能，当前版本{AppData.VERSION}",
                                QMessageBox.Ok,
                                QMessageBox.Ok)

    def export_setting(self):
        QMessageBox.information(self, "即将推出！", f"即将在v2.0.1版本推出此功能，当前版本{AppData.VERSION}",
                                QMessageBox.Ok,
                                QMessageBox.Ok)

    ###################################
    # Export #########################
    ###################################
    def pure_table_csv_export(self):
        QMessageBox.information(self, "即将推出！", f"即将在v2.0.2版本推出此功能，当前版本{AppData.VERSION}",
                                QMessageBox.Ok,
                                QMessageBox.Ok)
        # path, type_ = QFileDialog.getSaveFileName(self, '导出单词组', DictionaryData.current_word_list.group_name,
        #                                           "csv (*.csv)")
        # if path:
        #     self.model.pure_table_csv_export(path)

    def pure_table_excel_export(self):
        QMessageBox.information(self, "即将推出！", f"即将在v2.0.2版本推出此功能，当前版本{AppData.VERSION}",
                                QMessageBox.Ok,
                                QMessageBox.Ok)

    def meaning_word_export(self):
        QMessageBox.information(self, "即将推出！", f"即将在v2.0.2版本推出此功能，当前版本{AppData.VERSION}",
                                QMessageBox.Ok,
                                QMessageBox.Ok)

    def meaning_pdf_export(self):
        QMessageBox.information(self, "即将推出！", f"即将在v2.0.2版本推出此功能，当前版本{AppData.VERSION}",
                                QMessageBox.Ok,
                                QMessageBox.Ok)

    def spell_word_export(self):
        QMessageBox.information(self, "即将推出！", f"即将在v2.0.2版本推出此功能，当前版本{AppData.VERSION}",
                                QMessageBox.Ok,
                                QMessageBox.Ok)

    def spell_pdf_export(self):
        QMessageBox.information(self, "即将推出！", f"即将在v2.0.2版本推出此功能，当前版本{AppData.VERSION}",
                                QMessageBox.Ok,
                                QMessageBox.Ok)

    ###################################
    # Help ############################
    ###################################
    def show_help_tech_dialog_help(self):
        HelpTechController(self)

    def show_about_dialog_help(self):
        AboutController(self)

    def show_support_dialog_help(self):
        SupportController(self)
