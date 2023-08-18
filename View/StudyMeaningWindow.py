# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../UI/StudyMeaningWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(647, 533)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.word_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(50)
        self.word_label.setFont(font)
        self.word_label.setText("")
        self.word_label.setAlignment(QtCore.Qt.AlignCenter)
        self.word_label.setObjectName("word_label")
        self.verticalLayout.addWidget(self.word_label)
        self.tip_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.tip_label.setFont(font)
        self.tip_label.setText("")
        self.tip_label.setAlignment(QtCore.Qt.AlignCenter)
        self.tip_label.setObjectName("tip_label")
        self.verticalLayout.addWidget(self.tip_label)
        self.play_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.play_pushButton.setObjectName("play_pushButton")
        self.verticalLayout.addWidget(self.play_pushButton)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.no_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.no_pushButton.setObjectName("no_pushButton")
        self.horizontalLayout.addWidget(self.no_pushButton)
        self.tip_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.tip_pushButton.setObjectName("tip_pushButton")
        self.horizontalLayout.addWidget(self.tip_pushButton)
        self.yes_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.yes_pushButton.setObjectName("yes_pushButton")
        self.horizontalLayout.addWidget(self.yes_pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "背单词"))
        self.play_pushButton.setText(_translate("MainWindow", "播放音频"))
        self.no_pushButton.setText(_translate("MainWindow", "不会"))
        self.tip_pushButton.setText(_translate("MainWindow", "提示"))
        self.yes_pushButton.setText(_translate("MainWindow", "会"))
