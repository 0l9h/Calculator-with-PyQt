class math_operations():
    
    def addition(self):
        self.killExcessiveElement()
        self.checkout()      #   check if user chose operation before
        self.op = '+'
        self.pushButton_PLUS.setStyleSheet('color: red')


    def subtraction(self):
        self.killExcessiveElement()
        self.checkout()
        self.op = '-'
        self.pushButton_MINUS.setStyleSheet('color: red')      #    Set red color to button that user has clicked


    def multiply(self):
        self.killExcessiveElement()
        self.checkout()      
        self.op = '*'
        self.pushButton_MULTIPLY.setStyleSheet('color: red')


    def divide(self):
        self.killExcessiveElement()
        self.checkout()      
        self.op = '/'
        self.pushButton_DIVIDE.setStyleSheet('color: red')


    def delete(self):
        self.op = ''
        self.lineEdit.setText('0')
        self.values_list = [0]

        
    def equals(self):
        self.killExcessiveElement()
        if len(self.values_list) == 2:
            self.checkout()
        else:
            self.answer = self.values_list[0]

        self.lineEdit.setText(str(self.answer))