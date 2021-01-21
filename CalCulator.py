from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CalCulator"), self.setGeometry(50,50,100,230), self.setMaximumSize(250,270), self.setWindowIcon(QIcon("calc.png"))

        #self.qisqa_usul()             # 2-usul kodini ishga tushirish
        self.keypad()                # 1-usul kodini ishga tushirish
        self.temp_num = []
        self.fin_num = []

    def keypad(self):                # 1-usul kod kurinishi
        self.vbox = QVBoxLayout(self)
        self.grid = QGridLayout(self)


        self.result = QLineEdit()
        self.result.setPlaceholderText("CalCulaTor")
        self.bn_result = QPushButton("Enter", clicked=self.natija)
        self.clear = QPushButton("Clear", clicked=self.clear_cal)
        self.back = QPushButton("◄ Back", clicked=self.back)
        self.b1 = QPushButton("1",clicked= lambda:self.num_pres("1"))
        self.b2 = QPushButton("2", clicked= lambda:self.num_pres("2"))
        self.b3 = QPushButton("3", clicked= lambda:self.num_pres("3"))
        self.b4 = QPushButton("4", clicked= lambda:self.num_pres("4"))
        self.b5 = QPushButton("5", clicked= lambda:self.num_pres("5"))
        self.b6 = QPushButton("6", clicked= lambda:self.num_pres("6"))
        self.b7 = QPushButton("7", clicked= lambda:self.num_pres("7"))
        self.b8 = QPushButton("8", clicked= lambda:self.num_pres("8"))
        self.b9 = QPushButton("9", clicked= lambda:self.num_pres("9"))
        self.b0 = QPushButton("0", clicked= lambda:self.num_pres("0"))
        self.plus = QPushButton("+", clicked=lambda: self.funk_pres("+"))
        self.minus = QPushButton("-", clicked=lambda: self.funk_pres("-"))
        self.mult = QPushButton("x", clicked=lambda: self.funk_pres("*"))
        self.divd = QPushButton("÷", clicked=lambda: self.funk_pres("/"))
        self.yul = QPushButton("*", clicked=lambda: self.funk_pres("*"))
        self.resh = QPushButton("#", clicked=lambda: self.funk_pres("#"))

        self.grid.addWidget(self.result,0,0, 1,4)
        self.grid.addWidget(self.bn_result,1,0, 1,2)
        self.grid.addWidget(self.clear,1,3)
        self.grid.addWidget(self.back,1,2)
        self.grid.addWidget(self.b1,2,0)
        self.grid.addWidget(self.b2,2,1)
        self.grid.addWidget(self.b3,2,2)
        self.grid.addWidget(self.plus, 2, 3)
        self.grid.addWidget(self.b4,3,0)
        self.grid.addWidget(self.b5,3,1)
        self.grid.addWidget(self.b6,3,2)
        self.grid.addWidget(self.minus, 3, 3)
        self.grid.addWidget(self.b7,4,0)
        self.grid.addWidget(self.b8,4,1)
        self.grid.addWidget(self.b9,4,2)
        self.grid.addWidget(self.mult, 4, 3)
        self.grid.addWidget(self.yul, 5, 0)
        self.grid.addWidget(self.b0, 5,1)
        self.grid.addWidget(self.resh, 5,2)
        self.grid.addWidget(self.divd,5,3)
        self.vbox.addLayout(self.grid)

    def qisqa_usul(self):                # 1-usul kod kurinishi
        self.vbox = QVBoxLayout()
        self.hbox = QHBoxLayout()
        self.fbox = QFormLayout(self)
        self.grid = QGridLayout(self)


        self.result = QLineEdit()
        self.result.setPlaceholderText("CalCulaTor")
        self.bn_result = QPushButton("Enter", clicked=self.natija)
        self.clear = QPushButton("Clear", clicked=self.clear_cal)
        self.back = QPushButton("◄ Back", clicked=self.back)
        self.hbox.addWidget(self.bn_result)
        self.hbox.addWidget(self.back)
        self.hbox.addWidget(self.clear)

        self.plus = QPushButton("+", clicked=lambda: self.funk_pres("+"))
        self.minus = QPushButton("-", clicked=lambda: self.funk_pres("-"))
        self.mult = QPushButton("x", clicked=lambda: self.funk_pres("*"))
        self.divd = QPushButton("÷", clicked=lambda: self.funk_pres("/"))
        self.grid.addWidget(self.plus, 1,3)
        self.grid.addWidget(self.minus, 2,3)
        self.grid.addWidget(self.mult, 3,3)
        self.grid.addWidget(self.divd, 4,3)


        names = [
                 '1', '2', '3',
                 '4', '5', '6',
                 '7', '8', '9',
                 '*', '0', '#']

        self.fbox.addRow(self.result)
        self.fbox.addRow(self.hbox)

        joylashish = [(i, j) for i in range(1,6) for j in range(3)]
        for joylan, name in zip(joylashish, names):
            self.but = QPushButton((name), clicked = lambda: name)
            #self.but.clicked.connect(lambda: self.num_pres((name)))
            self.grid.addWidget(self.but, *joylan)
        self.fbox.addRow(self.grid)




            # QPushButton("1",clicked= lambda:self.num_pres("1"))

    def num(self, keypad):
        pass

    def num_pres(self, keynum):
        try:
            text = self.result.text()
            self.result.append("%s = <font color=blue> %s </font>" %(text, eval(text)) )
        except:
            self.result.setText(text)
    def funk_pres(self, operator):
        tempstring = "".join(self.temp_num)
        self.fin_num.append(tempstring)
        self.fin_num.append(operator)
        self.temp_num = []
        self.result.setText("".join(self.fin_num))
    def natija(self):
        finstring = "".join(self.fin_num) + "".join(self.temp_num)
        resultstring = eval(finstring)
        finstring += "="
        finstring += str(resultstring)
        self.result.setText(finstring)
    def clear_cal(self):
        self.result.clear()
        self.temp_num = []
        self.fin_num = []

    def back(self):
        #a=self.result.text()


        a = ["l"]
        x = 0
        for back in self.result.text():
            if x < (int(len(self.result.text())) - 1):
                a.append(back)
                a[0] += a[1]
                a.remove(a[-1])
            x += 1
        b = str(a).strip("l[]''")

        self.result.text().replace(self.result.text(),b)
        print(type(b), "b=",b)
        print(type(self.result.text()), "a=", self.result.text())
        self.result.textChanged((str(a).strip("l[]''")))

a = QApplication([])
a.setStyle(QStyleFactory.create("Fusion"))
ekran = Window()
ekran.show()
a.exec_()
