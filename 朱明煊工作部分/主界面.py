# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '主界面.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import bgimag
import imag


class Ui_FormMain(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(632, 395)
        #Form.setStyleSheet("background-image: url(:/imgTest/bg1.jpg);")
        self.listView = QtWidgets.QListView(Form)
        self.listView.setGeometry(QtCore.QRect(50, 50, 141, 151))
        #self.listView.setStyleSheet("background-image: url(:/Test/bgimg/bg5.jpg);")
        self.listView.setObjectName("listView")
        self.pushButton5 = QtWidgets.QPushButton(Form)
        self.pushButton5.setGeometry(QtCore.QRect(50, 10, 140, 30))
        font = QtGui.QFont()
        font.setFamily("Yuppy SC")
        self.pushButton5.setFont(font)
        self.pushButton5.setMouseTracking(True)
        #self.pushButton5.setStyleSheet("background-image: url(:/Test/bgimg/bg5.jpg);")
        self.pushButton5.setObjectName("pushButton5")
        self.pushButton_25 = QtWidgets.QPushButton(Form)
        self.pushButton_25.setGeometry(QtCore.QRect(380, 10, 140, 30))
        font = QtGui.QFont()
        font.setFamily("Yuppy SC")
        self.pushButton_25.setFont(font)
        self.pushButton_25.setMouseTracking(True)
        #self.pushButton_25.setStyleSheet("background-image: url(:/Test/bgimg/bg5.jpg);")
        self.pushButton_25.setObjectName("pushButton_25")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(380, 60, 241, 81))
        #self.textBrowser.setStyleSheet("background-image: url(:/Test/bgimg/bg5.jpg);")
        self.textBrowser.setObjectName("textBrowser")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 210, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Yuppy SC")
        font.setPointSize(14)
        self.label.setFont(font)
        #self.label.setStyleSheet("background-image: url(:/Test/bgimg/bg5.jpg);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 250, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Yuppy SC")
        font.setPointSize(14)
        self.label_2.setFont(font)
        #self.label_2.setStyleSheet("background-image: url(:/Test/bgimg/bg5.jpg);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 290, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Yuppy SC")
        font.setPointSize(14)
        self.label_3.setFont(font)
        #self.label_3.setStyleSheet("background-image: url(:/Test/bgimg/bg5.jpg);")
        self.label_3.setObjectName("label_3")
        self.pushButton_35 = QtWidgets.QPushButton(Form)
        self.pushButton_35.setMouseTracking(True)
        self.pushButton_35.setGeometry(QtCore.QRect(10, 340, 101, 31))
        #self.pushButton_35.setStyleSheet("background-image: url(:/Test/bgimg/bg5.jpg);")
        self.pushButton_35.setObjectName("pushButton_35")
        self.pushButton_45 = QtWidgets.QPushButton(Form)
        self.pushButton_45.setMouseTracking(True)
        self.pushButton_45.setGeometry(QtCore.QRect(130, 340, 101, 31))
        # self.pushButton_35.setStyleSheet("background-image: url(:/Test/bgimg/bg5.jpg);")
        self.pushButton_45.setObjectName("pushButton_45")
        self.pushButton_55 = QtWidgets.QPushButton(Form)
        self.pushButton_55.setMouseTracking(True)
        self.pushButton_55.setGeometry(QtCore.QRect(250, 340, 101, 31))
        # self.pushButton_35.setStyleSheet("background-image: url(:/Test/bgimg/bg5.jpg);")
        self.pushButton_55.setObjectName("pushButton_45")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(370, 330, 31, 21))
        font = QtGui.QFont()
        font.setFamily("Yuppy SC")
        font.setPointSize(14)
        self.label_4.setFont(font)
        #self.label_4.setStyleSheet("background-image: url(:/Test/bgimg/bg5.jpg);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(530, 330, 31, 21))
        font = QtGui.QFont()
        font.setFamily("Yuppy SC")
        font.setPointSize(14)
        self.label_5.setFont(font)
        #self.label_5.setStyleSheet("background-image: url(:/Test/bgimg/bg5.jpg);")
        self.label_5.setObjectName("label_5")
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(370, 300, 191, 31))
        #self.progressBar.setStyleSheet("background-image: url(:/Test/bgimg/bg5.jpg);")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.textBrowser_2 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_2.setGeometry(QtCore.QRect(80, 210, 141, 31))
        #self.textBrowser_2.setStyleSheet("background-image: url(:/Test/bgimg/bg5.jpg);")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_3.setGeometry(QtCore.QRect(80, 250, 141, 31))
        #self.textBrowser_3.setStyleSheet("background-image: url(:/Test/bgimg/bg5.jpg);")
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textBrowser_4 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_4.setGeometry(QtCore.QRect(80, 290, 141, 31))
        #self.textBrowser_4.setStyleSheet("background-image: url(:/Test/bgimg/bg5.jpg);")
        self.textBrowser_4.setObjectName("textBrowser_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton5.setText(_translate("Form", "个人测温数据统计"))
        self.pushButton_25.setText(_translate("Form", "区域测温数据统计"))
        self.label.setText(_translate("Form", "姓名："))
        self.label_2.setText(_translate("Form", "体温："))
        self.label_3.setText(_translate("Form", "时间："))
        self.pushButton_35.setText(_translate("Form", "播报"))
        self.pushButton_45.setText(_translate("Form", "打开摄像头"))
        self.pushButton_55.setText(_translate("Form", "测温"))
        self.label_4.setText(_translate("Form", "安全"))
        self.label_5.setText(_translate("Form", "危险"))
