import random
from functools import partial
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtCore import QFile
from ui_mainwindow import Ui_MainWindow



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_roo.clicked.connect(partial (self.play , "onhand"))
        self.ui.btn_back.clicked.connect(partial (self.play , "backhand"))
        self.status="player"
        self.boy_score=0
        self.girl_score=0
        self.user_score=0
        self.counter=0

    def play(self,x):
        if self.status=="player":
            self.ui.user.setText(x)
            self.status="girl"
        if self.status=="girl":
            self.girl_choice=random.randint(1,2)
            if self.girl_choice==1:
                self.ui.girl.setText("onhand")
                self.status="boy"
            elif self.girl_choice==2:
                self.ui.girl.setText("backhand")
                self.status="boy"
        if self.status=="boy":
            self.boy_choice=random.randint(1,2)
            if self.boy_choice==1:
                self.ui.boy.setText("onhand")
                self.status="player"
                self.check()
            elif self.boy_choice==2:
                self.ui.boy.setText("backhand")
                self.status="player"
                self.check()


    def check(self):
    
        if self.ui.user.text()== self.ui.girl.text()!=self.ui.boy.text():
            self.boy_score +=1
            self.ui.boy_score.setText(str(self.boy_score))
            self.ui.result.setText("boy win")
            self.counter+=1
            self.win()

        elif self.ui.user.text()==self.ui.boy.text()!=self.ui.girl.text():
            self.girl_score +=1
            self.ui.girl_score.setText(str(self.girl_score))
            self.ui.result.setText("girl win")
            self.counter+=1
            self.win()

        elif self.ui.girl.text()==self.ui.boy.text()!=self.ui.user.text():
            self.user_score +=1
            self.ui.user_score.setText(str(self.user_score))
            self.ui.result.setText("You win")  
            self.counter+=1
            self.win()

        elif self.ui.girl.text()==self.ui.boy.text()==self.ui.user.text():
            self.user_score = self.user_score
            self.girl_score=self.girl_score
            self.boy_score=self.boy_score 
            self.ui.result.setText(" ")
            self.counter+=1
            self.win()


    def win(self):
   
     if self.counter==5:
        if int(self.user_score) > int(self.girl_score) and int(self.user_score) > int(self.boy_score) or int(self.user_score) > int(self.girl_score) == int(self.boy_score):
            self.ui.result.setText("🎉YOU WIN🎉")
            self.clear()

        elif int(self.girl_score) > int(self.user_score) and int(self.girl_score) > int(self.boy_score) or int(self.girl_score) > int(self.user_score) == int(self.boy_score):
            self.ui.result.setText("🎉GIRL WIN🎉")
            self.clear()

        elif int(self.boy_score) > int(self.user_score) and int(self.boy_score) > int(self.girl_score) or int(self.boy_score) > int(self.user_score) == int(self.girl_score):
            self.ui.result.setText("🎉BOY WIN🎉")
            self.clear()

        elif int(self.girl_score) < int(self.boy_score) == int(self.user_score) or int(self.user_score) < int(self.boy_score) == int(self.girl_score) or int(self.boy_score)< int(self.girl_score) == int(self.user_score) or int(self.boy_score) == int(self.user_score) == int(self.girl_score):
            self.ui.result.setText("NO WINNER")
            self.clear()




    def clear(self):
            msg_box=QMessageBox()
            msg_box.setText("play again?")
            msg_box.exec()
            self.user_score=0
            self.girl_score=0
            self.boy_score=0
            self.ui.user_score.setText("")
            self.ui.boy_score.setText("")
            self.ui.girl_score.setText("")
            self.ui.boy.setText("")
            self.ui.girl.setText("")
            self.ui.user.setText("")
            self.ui.result.setText("")


app=QApplication(sys.argv)
window=MainWindow()
window.show()



app.exec()