import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from interface import Ui_Form
from operations import math_operations
from math import ceil


class Example(Ui_Form, math_operations):

    values_list = []
    line = ''
    op = ''

    def Connection(self):
        self.pushButton_0.clicked.connect(self.num_button_clicked)
        self.pushButton_1.clicked.connect(self.num_button_clicked)
        self.pushButton_2.clicked.connect(self.num_button_clicked)
        self.pushButton_3.clicked.connect(self.num_button_clicked)
        self.pushButton_4.clicked.connect(self.num_button_clicked)
        self.pushButton_5.clicked.connect(self.num_button_clicked)
        self.pushButton_6.clicked.connect(self.num_button_clicked)
        self.pushButton_7.clicked.connect(self.num_button_clicked)
        self.pushButton_8.clicked.connect(self.num_button_clicked)
        self.pushButton_9.clicked.connect(self.num_button_clicked)
        self.pushButton_PLUS.clicked.connect(self.op_button_clicked)
        self.pushButton_MINUS.clicked.connect(self.op_button_clicked)
        self.pushButton_MULTIPLY.clicked.connect(self.op_button_clicked)
        self.pushButton_DIVIDE.clicked.connect(self.op_button_clicked)
        self.pushButton_EQUALS.clicked.connect(self.op_button_clicked)
        self.pushButton_DEL.clicked.connect(self.op_button_clicked)
    

    def num_button_clicked(self):
        sender = self.sender()
        self.line += sender.text()      #   Get button value
        self.lineEdit.setText(self.line)        #   Write new value into lineEdit


    def op_button_clicked(self):
        self.pushButton_PLUS.setStyleSheet('color: #4a4a4a')    #   Set default color to operation buttons
        self.pushButton_MINUS.setStyleSheet('color: #4a4a4a')
        self.pushButton_MULTIPLY.setStyleSheet('color: #4a4a4a')
        self.pushButton_DIVIDE.setStyleSheet('color: #4a4a4a')
        sender = self.sender()
        self.del_all()
        if sender.text() == '+':
            self.addition()
        elif sender.text() == '-':
            self.subtraction()
        elif sender.text() == '*':
            self.multiply()
        elif sender.text() == '/':
            self.divide()
        elif sender.text() == '=':
            self.equals()
        elif sender.text() == 'DEL':
            self.delete()
        print(self.values_list)


    def del_all(self):
        if len(self.line)>0:
            self.var = float(self.line)       #   Convert str into int
            self.values_list.append(self.var)       #   Add new number to list
        sender = self.sender()
        self.line = sender.text()
        self.lineEdit.setText(self.line)
        self.line = ''      #   If user chooses operation, delete all chars from display


    def getAnswer(self):
        self.values_list.clear()
        self.values_list.append(str(self.answer))   #   Get answer
        self.lineEdit.setText(self.values_list[0])


    def checkout(self):
        if self.op == '+':                                                  #   If user wrote "+" before
            self.answer = float(self.values_list[0]) + self.values_list[1]    #   Add two numbers
            self.getAnswer()                                                #   get Answer
            self.op = ''
        elif self.op == '-':
            self.answer = float(self.values_list[0]) - self.values_list[1]
            self.getAnswer()
            self.op = ''
        elif self.op == '*':
            self.answer = float(self.values_list[0]) * self.values_list[1]
            self.getAnswer()
            self.op = ''
        elif self.op == '/':
            self.answer = float(self.values_list[0]) / self.values_list[1]
            self.getAnswer()
            self.op = ''




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Example()
    ui.setupUi(Form)
    ui.Connection()
    Form.show()
    sys.exit(app.exec_())