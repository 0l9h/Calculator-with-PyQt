# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculator.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(QtWidgets.QMainWindow):



    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(525, 361)
        Form.setStyleSheet("QPushButton{\n"
"    width: 50px;\n"
"    height: 50px;\n"
"    font-size: 25px;\n"
"    font-weight: bold;\n"
"    color: rgb(74, 74, 74);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: silver;\n"
"}\n"
"\n"
"QLabel{\n"
"    background-color: rgb(188, 188, 188)\n"
"}\n"
"\n"
"")
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(90, 20, 320, 333))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_MULTIPLY = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_MULTIPLY.setObjectName("pushButton_MULTIPLY")
        self.gridLayout.addWidget(self.pushButton_MULTIPLY, 5, 3, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 5, 1, 1, 1)
        self.pushButton_DEL = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_DEL.setObjectName("pushButton_DEL")
        self.gridLayout.addWidget(self.pushButton_DEL, 6, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 3, 1, 1, 1)
        self.pushButton_0 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_0.setIconSize(QtCore.QSize(16, 16))
        self.pushButton_0.setObjectName("pushButton_0")
        self.gridLayout.addWidget(self.pushButton_0, 6, 1, 1, 1)
        self.pushButton_PLUS = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_PLUS.setObjectName("pushButton_PLUS")
        self.gridLayout.addWidget(self.pushButton_PLUS, 3, 3, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 4, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label.setStyleSheet("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 4)
        self.pushButton_MINUS = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_MINUS.setObjectName("pushButton_MINUS")
        self.gridLayout.addWidget(self.pushButton_MINUS, 4, 3, 1, 1)
        self.pushButton_DIVIDE = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_DIVIDE.setObjectName("pushButton_DIVIDE")
        self.gridLayout.addWidget(self.pushButton_DIVIDE, 6, 3, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 4, 1, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 4, 0, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 5, 0, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_9, 5, 2, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 3, 2, 1, 1)
        self.lineEdit = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lineEdit.setStyleSheet("QLabel{\n"
"    height: 30px;\nbackground-color: #6ebfb8;\nfont: 75 16pt 'Palatino Linotype';\n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 2, 0, 1, 4)
        self.pushButton_EQUALS = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_EQUALS.setObjectName("pushButton_EQUALS")
        self.gridLayout.addWidget(self.pushButton_EQUALS, 6, 2, 1, 1)
        self.pushButton_1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_1.sizePolicy().hasHeightForWidth())
        self.pushButton_1.setSizePolicy(sizePolicy)
        self.pushButton_1.setStyleSheet("")
        self.pushButton_1.setObjectName("pushButton_1")
        self.gridLayout.addWidget(self.pushButton_1, 3, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Calculator"))
        self.pushButton_MULTIPLY.setText(_translate("Form", "*"))
        self.pushButton_8.setText(_translate("Form", "8"))
        self.pushButton_DEL.setText(_translate("Form", "DEL"))
        self.pushButton_2.setText(_translate("Form", "2"))
        self.pushButton_0.setText(_translate("Form", "0"))
        self.pushButton_PLUS.setText(_translate("Form", "+"))
        self.pushButton_6.setText(_translate("Form", "6"))
        self.label.setText(_translate("Form", "CALCULATOR"))
        self.pushButton_MINUS.setText(_translate("Form", "-"))
        self.pushButton_DIVIDE.setText(_translate("Form", "/"))
        self.pushButton_5.setText(_translate("Form", "5"))
        self.pushButton_4.setText(_translate("Form", "4"))
        self.pushButton_7.setText(_translate("Form", "7"))
        self.pushButton_9.setText(_translate("Form", "9"))
        self.pushButton_3.setText(_translate("Form", "3"))
        self.pushButton_EQUALS.setText(_translate("Form", "="))
        self.pushButton_1.setText(_translate("Form", "1"))

