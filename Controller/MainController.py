import shutil
import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import QUrl, QModelIndex, Qt, QCoreApplication
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtWidgets import QMainWindow, QInputDialog, QTableWidget, QTableWidgetItem, QPushButton, QMessageBox, \
    QListWidgetItem, QFileDialog, QProgressDialog

from Controller.BatchWordController import BatchWordController
from Controller.EditWordController import EditWordController
from Controller.StudyMeaningController import TestController
from Model.MainModel import MainModel
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


    def init(self):
        # 设置表格不可编辑
        self.word_tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)
        # 默认单选
        self.word_tableWidget.setSelectionMode(QTableWidget.SingleSelection)
        # Create a media player instance
        self.media_player = QMediaPlayer()

        self.init_group()

    def short_key_connect(self):
        ...

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
        selected_items = self.group_listWidget.selectedItems()
        if selected_items:
            for item in selected_items:
                self.model.delete_group(item.text())
        if not self.group_listWidget.size().isEmpty():
            self.model.load_word(self.group_listWidget.item(0).text())
            self.update_word()
        else:
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
                self.word_tableWidget.setCurrentItem(self.word_tableWidget.item(self.word_tableWidget.rowCount()-1,0))
            else:
                QMessageBox.information(self, "提示", f"单词{text}重复", QMessageBox.Ok, QMessageBox.Ok)

    def add_inauto_word(self):
        text, ok = QInputDialog.getText(self, '添加单词', '请输入要手动添加的单词')
        if ok:
            if not self.model.is_exist_word(text):
                self.model.add_inauto_word(text)
                self.update_word()
                self.word_tableWidget.setCurrentItem(self.word_tableWidget.item(self.word_tableWidget.rowCount()-1,0))
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
        play_button.clicked.connect(lambda: self.player_online_radio(audio_link))
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
        TestController(DictionaryData.current_word_list.group_name, self)

    ###################################
    # Other ###########################
    ###################################
    def player_online_radio(self, link):
        audio = QMediaContent(QUrl(link))
        self.media_player.setMedia(audio)
        self.media_player.play()

    def closeEvent(self, a0):
        super().closeEvent(a0)
        self.model.save_word()