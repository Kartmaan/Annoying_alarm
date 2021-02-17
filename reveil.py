import sys
from datetime import datetime, timedelta
import time
import random
import threading

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox

from reveil_win import Ui_MainWindow

""" Total threads :
1/ thd.time : link to curr_time() -> Current time display
2/ thd.wait : link to waiting() -> Wait to ring
3/ thd.lcd : link to lcd_numbers -> Rolling numbers
"""

run = True
waiting = 0
unknown_x = None

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.button_validation.clicked.connect(self.validation)
        self.button_stop.clicked.connect(self.stop)
        self.lineEdit.textChanged.connect(self.equation_edit)

        self.thd_time = threading.Thread(target=self.curr_time)
        self.thd_time.start()

        self.set_timeEdit()
    
    def curr_time(self):
        """ Current time display """

        global run
        time_format = "%H:%M:%S"

        while run:
            today = datetime.now()
            hour = today.strftime(time_format)
            self.label_currTime.setText(hour)
            time.sleep(0.08)

            if run == False:
                break
    
    def set_timeEdit(self):
        """ TimeEdit initialisation """

        now = datetime.now()
        later = now + timedelta(minutes = 1)
        hour = int(later.strftime("%H"))
        minute = int(later.strftime("%M"))
        self.timeEdit.setTime(QtCore.QTime(hour, minute, 0))
    
    def validation(self):
        """ Validation button behaviour """
        global waiting

        if waiting == True:
            waiting = False
            self.thd_wait.join()

        self.thd_wait = threading.Thread(target=self.waiting)
        self.thd_wait.start()

        #if waiting == None:
        #    waiting = True
        #if waiting == True:
        #    waiting = False

        #self.thd_lcd = threading.Thread(target=self.lcd_numbers)
        #self.thd_lcd.start()
    
    def stop(self):
        """ Button stop behaviour """

        self.button_validation.setEnabled(True)

        # Reinitialisations
        self.button_stop.setEnabled(False)
        self.lcd_oper.setProperty("intValue", 0)
        self.lcd_res.setProperty("intValue", 0)
        self.label_operator.setText(".")
        self.lineEdit.clear()
    
    def waiting(self):
        """ Waiting for the ring """

        global run, waiting # Test

        #if waiting == 0:
        #    waiting = True

        edited_h = self.timeEdit.time().hour()
        if len(str(edited_h)) == 1:
            x = ["0",str(edited_h)]
            edited_h = "".join(x)
            print(edited_h)

        edited_m = self.timeEdit.time().minute()
        if len(str(edited_m)) == 1:
            x = ["0",str(edited_m)]
            edited_m = "".join(x)
            print(edited_m)

        edited_time = f"{edited_h}:{edited_m}"
        print(edited_time)

        ring = False
        waiting = True

        while ring == False: 
            today = datetime.now()
            currHour = today.strftime("%H:%M")
            print(f"curr = {currHour}, targ = {edited_time}")

            if run == False or waiting == False: # TEST
                break

            if currHour == edited_time:
                ring == True
                self.button_validation.setEnabled(False)
                print("RING !")
                self.equation_gen()
                waiting = False # TEST
                break
            
            else :
                time.sleep(1)
                continue
    
    def equation_gen(self):
        """ Generate the equation """

        global unknown_x
        
        operators = ["+", "-"]
        op = random.choice(operators)

        if op == "+":
            self.label_operator.setText(op)
            a = random.randint(10,99)
            x = random.randint(10,99)
            res = a + x

        if op == "-":
            self.label_operator.setText(op)
            while True:
                frst = random.randint(10,99)
                scnd = random.randint(10,99)
                if abs(frst-scnd) < 8:
                    continue
                else:
                    break

            a = max([frst, scnd])
            x = min([frst, scnd])
            res = a - x

        unknown_x = x
        print(unknown_x)

        #print(f"{a}{op}{x}={res}")
        self.thd_lcd = threading.Thread(target=self.lcd_numbers, args=(a, res))
        self.thd_lcd.start()
        #self.lcd_numbers(a, res)


    def equation_edit(self):
        """ Get the choice of the unknown in the equation """

        choice = self.lineEdit.text()
        print(choice)
        if choice == str(unknown_x):
            print("Match")
            self.button_stop.setEnabled(True)
        else:
            print("No match")
            self.button_stop.setEnabled(False)
    
    def lcd_numbers(self, a, res):
        """ Rolling numbers """

        i = 0
        while i<20:
            x = random.randint(10,99)
            self.lcd_oper.setProperty("intValue", x)
            i+=1
            time.sleep(0.05)
        self.lcd_oper.setProperty("intValue", a)

        i = 0
        while i<20:
            x = random.randint(10,99)
            self.lcd_res.setProperty("intValue", x)
            i+=1
            time.sleep(0.05)
        self.lcd_res.setProperty("intValue", res)
    
    def closeEvent(self, event):
        """ When user wants to quit """

        global run

        reply = QMessageBox.question(self, 'Window Close', 'Exit the program ?', 
        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
            run = False
            print('Window closed')
        else:
            event.ignore()

if __name__ == "__main__" :
	app = QtWidgets.QApplication(sys.argv) # []
	main_window = MainWindow()
	main_window.show()
	sys.exit(app.exec_())