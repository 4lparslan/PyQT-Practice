from PyQt5.QtWidgets import *
from calc import Ui_Form

class Calculator(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.counting = Ui_Form()
        self.counting.setupUi(self)
        self.memory = list()
        self.tempNum = None

        #self.counting.lcdNumber.display("0510")

        self.counting.pushButton0.clicked.connect(lambda : self.Memory(number="0"))
        self.counting.pushButton1.clicked.connect(lambda : self.Memory(number="1"))
        self.counting.pushButton2.clicked.connect(lambda : self.Memory(number="2"))
        self.counting.pushButton3.clicked.connect(lambda : self.Memory(number="3"))
        self.counting.pushButton4.clicked.connect(lambda : self.Memory(number="4"))
        self.counting.pushButton5.clicked.connect(lambda : self.Memory(number="5"))
        self.counting.pushButton6.clicked.connect(lambda : self.Memory(number="6"))
        self.counting.pushButton7.clicked.connect(lambda : self.Memory(number="7"))
        self.counting.pushButton8.clicked.connect(lambda : self.Memory(number="8"))
        self.counting.pushButton9.clicked.connect(lambda : self.Memory(number="9"))

        self.counting.pushButton_multi.clicked.connect(lambda: self.Memory(op="multi"))
        self.counting.pushButton_div.clicked.connect(lambda: self.Memory(op="div"))
        self.counting.pushButton_add.clicked.connect(lambda: self.Memory(op="add"))
        self.counting.pushButton_sub.clicked.connect(lambda: self.Memory(op="sub"))
        self.counting.pushButton_out.clicked.connect(lambda: self.Memory(op="out"))
        self.counting.pushButton_clear.clicked.connect(lambda: self.Memory(op="clear"))

    def Memory(self, number=None, op=None):
        if number != None:
            if self.tempNum != None:
                self.tempNum = self.tempNum + number
            else:
                self.tempNum = number
            print(self.tempNum)
            self.counting.lcdNumber.display(self.tempNum)


        if op != None:
            if self.tempNum != None:
                self.memory.append(int(self.tempNum))
                self.tempNum = None
            print(op)
            print(self.memory)

            if op == "clear":
                self.memory.clear()
                self.tempNum = None
                self.counting.lcdNumber.display(0)
            if op != "out" and op != "undo" and op != "clear":
                self.memory.append(op)
                print(self.memory)
                self.counting.lcdNumber.display(self.PrepareToDisplay())
            elif op == "out":
                the_outcome = self.Calculator(self.memory)
                self.counting.lcdNumber.display(the_outcome)



    def Calculator(self, the_list):
        if len(the_list) == 1:
            return the_list[0]
        if "multi" in the_list or "div" in the_list:
            for i in range(len(the_list)):
                if the_list[i] == "multi":
                    return self.Calculator(the_list[0:i-1] + [str(int(the_list[i-1])*int(the_list[i+1]))] + the_list[i+2:])
                elif the_list[i] == "div":
                    return self.Calculator(the_list[0:i - 1] + [str(float(the_list[i - 1]) / float(the_list[i + 1]))] + the_list[i + 2:])
        for i in range(len(the_list)):
            if the_list[i] == "add":
                return self.Calculator([str(int(the_list[i-1]) + int(the_list[i+1]))] + the_list[i+2:])
            elif the_list[i] == "sub":
                return self.Calculator([str(int(the_list[i-1]) - int(the_list[i+1]))] + the_list[i+2:])

    def PrepareToDisplay(self):
        total = ""
        for i in self.memory:
            if i == "add":
                total+="+"
            elif i == "sub":
                total+="-"
            elif i == "multi":
                total+="x"
            elif i == "div":
                total+="÷"
            else:
                total+=str(i)
        return total