import sys
from datetime import datetime, timedelta

from PyQt5 import QtWidgets, QtCore

from reveil_win import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.curr_time()
        self.set_timeEdit()
    
    def curr_time(self):
        time_format = "%H:%M:%S"
        today = datetime.now()
        hour = today.strftime(time_format)
        self.label_currTime.setText(hour)
    
    def set_timeEdit(self):
        now = datetime.now()
        later = now + timedelta(minutes = 20)
        hour = int(later.strftime("%H"))
        minute = int(later.strftime("%M"))
        self.timeEdit.setTime(QtCore.QTime(hour, minute, 0))




if __name__ == "__main__" :
	app = QtWidgets.QApplication(sys.argv) # []
	main_window = MainWindow()
	main_window.show()
	sys.exit(app.exec_())