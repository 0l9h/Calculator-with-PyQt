class AvoidBugs():    

    def delFirstZero(self):
        if str(self.line)[0] == '0' and len(str(self.line)) > 1:
            self.line = self.line[1:]       #   if number starts with '0' and != 0, delete first this zero


    def killExcessiveElement(self):
        if len(self.values_list) == 3:      #   deletes excessive element from values list, if it exists
            self.values_list.pop(0)