# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../UI/SettingDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(628, 527)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.groupBox = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.group_allow_multselect_checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.group_allow_multselect_checkBox.setChecked(True)
        self.group_allow_multselect_checkBox.setObjectName("group_allow_multselect_checkBox")
        self.verticalLayout_3.addWidget(self.group_allow_multselect_checkBox)
        self.group_ask_delete_checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.group_ask_delete_checkBox.setChecked(True)
        self.group_ask_delete_checkBox.setObjectName("group_ask_delete_checkBox")
        self.verticalLayout_3.addWidget(self.group_ask_delete_checkBox)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.group_auto_order_radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.group_auto_order_radioButton.setChecked(True)
        self.group_auto_order_radioButton.setObjectName("group_auto_order_radioButton")
        self.horizontalLayout_2.addWidget(self.group_auto_order_radioButton)
        self.group_reserve_auto_order_radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.group_reserve_auto_order_radioButton.setObjectName("group_reserve_auto_order_radioButton")
        self.horizontalLayout_2.addWidget(self.group_reserve_auto_order_radioButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_5.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.word_allow_multselect_checkBox = QtWidgets.QCheckBox(self.groupBox_2)
        self.word_allow_multselect_checkBox.setChecked(True)
        self.word_allow_multselect_checkBox.setObjectName("word_allow_multselect_checkBox")
        self.verticalLayout_4.addWidget(self.word_allow_multselect_checkBox)
        self.word_ask_delete_checkBox = QtWidgets.QCheckBox(self.groupBox_2)
        self.word_ask_delete_checkBox.setChecked(True)
        self.word_ask_delete_checkBox.setObjectName("word_ask_delete_checkBox")
        self.verticalLayout_4.addWidget(self.word_ask_delete_checkBox)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.word_auto_order_radioButton = QtWidgets.QRadioButton(self.groupBox_2)
        self.word_auto_order_radioButton.setChecked(True)
        self.word_auto_order_radioButton.setObjectName("word_auto_order_radioButton")
        self.horizontalLayout_3.addWidget(self.word_auto_order_radioButton)
        self.word_reserve_auto_order_radioButton = QtWidgets.QRadioButton(self.groupBox_2)
        self.word_reserve_auto_order_radioButton.setObjectName("word_reserve_auto_order_radioButton")
        self.horizontalLayout_3.addWidget(self.word_reserve_auto_order_radioButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.verticalLayout_5.addWidget(self.groupBox_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.audio_download_no_radioButton = QtWidgets.QRadioButton(self.tab)
        self.audio_download_no_radioButton.setObjectName("audio_download_no_radioButton")
        self.horizontalLayout.addWidget(self.audio_download_no_radioButton)
        self.audio_download_group_radioButton = QtWidgets.QRadioButton(self.tab)
        self.audio_download_group_radioButton.setObjectName("audio_download_group_radioButton")
        self.horizontalLayout.addWidget(self.audio_download_group_radioButton)
        self.audio_download_study_radioButton = QtWidgets.QRadioButton(self.tab)
        self.audio_download_study_radioButton.setChecked(True)
        self.audio_download_study_radioButton.setObjectName("audio_download_study_radioButton")
        self.horizontalLayout.addWidget(self.audio_download_study_radioButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.audio_download_save_network_checkBox = QtWidgets.QCheckBox(self.tab)
        self.audio_download_save_network_checkBox.setObjectName("audio_download_save_network_checkBox")
        self.horizontalLayout_4.addWidget(self.audio_download_save_network_checkBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.tabWidget.addTab(self.tab, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog", "单词组操作"))
        self.group_allow_multselect_checkBox.setText(_translate("Dialog", "允许多选（只适用于删除功能）"))
        self.group_ask_delete_checkBox.setText(_translate("Dialog", "删除确认"))
        self.group_auto_order_radioButton.setText(_translate("Dialog", "顺序排序"))
        self.group_reserve_auto_order_radioButton.setText(_translate("Dialog", "逆序排序"))
        self.groupBox_2.setTitle(_translate("Dialog", "单词本操作"))
        self.word_allow_multselect_checkBox.setText(_translate("Dialog", "允许多选（只适用于删除功能）"))
        self.word_ask_delete_checkBox.setText(_translate("Dialog", "删除确认"))
        self.word_auto_order_radioButton.setText(_translate("Dialog", "自动排序"))
        self.word_reserve_auto_order_radioButton.setText(_translate("Dialog", "逆序排序"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "操作设置"))
        self.audio_download_no_radioButton.setText(_translate("Dialog", "不缓存"))
        self.audio_download_group_radioButton.setText(_translate("Dialog", "查看单词组时缓存"))
        self.audio_download_study_radioButton.setText(_translate("Dialog", "学习单词时缓存（推荐）"))
        self.audio_download_save_network_checkBox.setText(_translate("Dialog", "省流量模式"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "音频缓存规则"))
