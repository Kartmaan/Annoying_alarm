# -*- coding: utf-8 -*-

""" 
A pesky alarm with a horrible ringing that can only be turned off 
by solving an equation

Threads :
1/ thd_time : link to curr_time() -> Current time display
2/ thd_wait : link to waiting() -> Wait the alarm
3/ thd_lcd : link to lcd_numbers -> Scrolling equation numbers
4/ thd_ring : link to alarm() -> Play alarm sound
5/ thd_blink : link to blinking_light() -> LED blinking during alarm
"""

import sys
from datetime import datetime, timedelta
import time
import random
import threading

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox
import simpleaudio as sa

from alarm_window import Ui_MainWindow

__author__ = "Kartmaan"
__version__ = "1.0"

run = True
waiting = 0
ring = False
unknown_x = None

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.button_validation.clicked.connect(self.validation)
        self.button_stop.clicked.connect(self.stop)
        self.lineEdit.textChanged.connect(self.equation_edit)

        # Start of the current time display threading 
        self.thd_time = threading.Thread(target=self.curr_time)
        self.thd_time.start()

        self.set_timeEdit() # TimeEdit initialisation
    
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
        """ TimeEdit initialisation
        Not far from current time """

        now = datetime.now()
        later = now + timedelta(minutes = 1)
        hour = int(later.strftime("%H"))
        minute = int(later.strftime("%M"))
        self.timeEdit.setTime(QtCore.QTime(hour, minute, 0))
    
    def validation(self):
        """ Validation button behaviour 
        Starts the waiting for alarm """

        global waiting

        """ If user validate while program already waiting for alarm,
        this wait is canceled to start another one """
        if waiting == True:
            waiting = False
            self.thd_wait.join()

        # Starting the waiting thread
        self.thd_wait = threading.Thread(target=self.waiting)
        self.thd_wait.start()
    
    def stop(self):
        """ Button stop behaviour
        Stops the alarm and reset some parameters """

        global ring

        ring = False # Set alarm OFF
        self.button_validation.setEnabled(True)

        # Reset
        self.button_stop.setEnabled(False)
        self.lcd_oper.setProperty("intValue", 0)
        self.lcd_res.setProperty("intValue", 0)
        self.label_operator.setText(".")
        self.lineEdit.clear()
        self.green_light.setEnabled(False)
        self.orange_light.hide()
        self.lineEdit.setEnabled(False)
    
    def waiting(self):
        """ Waiting for the alarm
        Waiting until current time = target time """

        global run, waiting, ring

        self.green_light.setEnabled(True) # Green LED ON

        """ When hour or minute is < 10, timeEdit widget returns
        something like 9:8 instead of 09:08. To avoid that, in that case, 
        we add a 0 as a prefix to respect the time syntax. """

        # Get the hour target
        edited_h = self.timeEdit.time().hour()
        if len(str(edited_h)) == 1:
            x = ["0", str(edited_h)]
            edited_h = "".join(x)

        # Get the minute target
        edited_m = self.timeEdit.time().minute()
        if len(str(edited_m)) == 1:
            x = ["0", str(edited_m)]
            edited_m = "".join(x)

        # Target time
        edited_time = f"{edited_h}:{edited_m}"
        print(edited_time)

        ring = False # Alarm is OFF
        waiting = True

        # Waiting until current time = target time
        while ring == False: 
            today = datetime.now()
            currHour = today.strftime("%H:%M")

            # Aborted wait
            # run = False : Program quited
            # waiting = False : Target time changed before alarm
            if run == False or waiting == False:
                break # Stop waiting

            # Current time = Targer time
            if currHour == edited_time:
                ring == True # Alarm is ON
                self.button_validation.setEnabled(False)
                print("RING !")

                # Alarm thread
                self.thd_ring = threading.Thread(target=self.alarm)
                self.thd_ring.start()

                # Blinking LED thread
                self.thd_blink = threading.Thread(target=self.blinking_light)
                self.thd_blink.start()

                self.equation_gen() # Generate an equation
                waiting = False # Stop waiting but alarm still ON
                
                break
            
            # Current time != target time
            # Wait continues
            else :
                time.sleep(1)
                continue
    
    def alarm(self):
        """ Play alarm sound """

        global ring
        ring = True 

        filename = './Files/alarm.wav'
        sound = sa.WaveObject.from_wave_file(filename)

        # Play sound while alarm is ON
        while ring == True:
            play = sound.play()
            play.wait_done()
    
    def blinking_light(self):
        """ Blinking LED light when alarm is ON. 
        Two images of the same dimensions have been superimposed 
        at the same coordinates : the image of the orange LED in the 
        foreground and that of the green LED in the background. 
        The background image (green LED) has been deactivated 
        to give it the appearance of an off LED (black & white). 
        Orange LED (foreground) is ON and appears and disappears 
        intermittently to give the appearance of a blinking LED """

        global ring

        self.green_light.setEnabled(False)

        # orange_light appears and disappears intermittently
        while ring:
            self.orange_light.show()
            time.sleep(0.3)
            self.orange_light.hide()
            time.sleep(0.3)
    
    def equation_gen(self):
        """ Generate the equation """

        global unknown_x
        
        minVal = 10
        maxVal = 299

        # Operator choice
        operators = ["+", "-"]
        op = random.choice(operators)

        if op == "+":
            self.label_operator.setText(op)
            a = random.randint(minVal, maxVal)
            x = random.randint(minVal, maxVal)
            res = a + x

        if op == "-":
            self.label_operator.setText(op)
            while True:
                frst = random.randint(minVal, maxVal)
                scnd = random.randint(minVal, maxVal)
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

    def equation_edit(self):
        """ Get the choice of the unknown in the equation """

        choice = self.lineEdit.text() # Get the enter
    
        if choice == str(unknown_x): # Right answer
            self.button_stop.setEnabled(True)

        else: # Wrong answer
            self.button_stop.setEnabled(False)
    
    def lcd_numbers(self, a, res):
        """ Random scrolling through numbers before 
        displaying the equation """

        # 1st number scrolling
        i = 0
        while i<20:
            x = random.randint(10,299)
            self.lcd_oper.setProperty("intValue", x)
            i+=1
            time.sleep(0.05)
        self.lcd_oper.setProperty("intValue", a)

        # Result number scrolling
        i = 0
        while i<20:
            x = random.randint(10,299)
            self.lcd_res.setProperty("intValue", x)
            i+=1
            time.sleep(0.05)
        self.lcd_res.setProperty("intValue", res)

        self.lineEdit.setEnabled(True)
    
    def closeEvent(self, event):
        """ When user wants to quit """

        global run, ring

        # When alarm is OFF, user can quit
        if ring == False: # Alarm is OFF

            reply = QMessageBox.question(self, 'Window Close', 'Akahaw ?', 
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

            if reply == QMessageBox.Yes:
                event.accept()
                run = False
                print('Window closed')
            else:
                event.ignore()
        
        # When alarm is ON, user can't quit
        if ring == True : # Alarm is ON

            reply = QMessageBox.question(self, 'Window Close', "O93od ghadi...", 
            QMessageBox.No | QMessageBox.No, QMessageBox.No)

            if reply == QMessageBox.No:
                event.ignore()
            else:
                event.ignore()

if __name__ == "__main__" :
	app = QtWidgets.QApplication(sys.argv) # []
	main_window = MainWindow()
	main_window.show()
	sys.exit(app.exec_())