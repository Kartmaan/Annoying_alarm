# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowTitle("Reveil pas sympa")

        MainWindow.resize(723, 459)
        MainWindow.setMinimumSize(QtCore.QSize(723, 459))
        MainWindow.setMaximumSize(QtCore.QSize(723, 459))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Time edit
        self.timeEdit = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEdit.setGeometry(QtCore.QRect(290, 180, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(33)
        self.timeEdit.setFont(font)
        self.timeEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.timeEdit.setTime(QtCore.QTime(13, 58, 0))
        #x = self.timeEdit.time().hour()
        #print(x)
        #self.timeEdit.setObjectName("timeEdit")

        # Horizontal line
        self.h_line = QtWidgets.QFrame(self.centralwidget)
        self.h_line.setGeometry(QtCore.QRect(-3, 250, 1011, 20))
        self.h_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.h_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        #self.h_line.setObjectName("line")

        # Title label
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(140, 20, 431, 31))
        self.label_title.setText("REVEIL PAS SYMPA")
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono Light")
        font.setPointSize(20)
        self.label_title.setFont(font)
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        #self.label_title.setObjectName("label_4")

        # Label "it's"
        self.label_its = QtWidgets.QLabel(self.centralwidget)
        self.label_its.setGeometry(QtCore.QRect(60, 140, 111, 31))
        self.label_its.setText("IL EST :")
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setItalic(True)
        self.label_its.setFont(font)
        self.label_its.setAlignment(QtCore.Qt.AlignCenter)
        #self.label_its.setObjectName("label")

        # Label current time
        self.label_currTime = QtWidgets.QLabel(self.centralwidget)
        self.label_currTime.setGeometry(QtCore.QRect(30, 190, 181, 41))
        self.label_currTime.setText("13:45:36")
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(33)
        self.label_currTime.setFont(font)
        self.label_currTime.setAlignment(QtCore.Qt.AlignCenter)
        #self.label_currTime.setObjectName("label_2")

        # Label "rings at"
        self.label_ringsAt = QtWidgets.QLabel(self.centralwidget)
        self.label_ringsAt.setGeometry(QtCore.QRect(320, 140, 116, 31))
        self.label_ringsAt.setText("SONNER A  :")
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setItalic(True)
        self.label_ringsAt.setFont(font)
        self.label_ringsAt.setAlignment(QtCore.Qt.AlignCenter)
        #self.label_ringsAt.setObjectName("label_3")

        # Button validation
        self.button_validation = QtWidgets.QPushButton(self.centralwidget)
        self.button_validation.setGeometry(QtCore.QRect(520, 180, 161, 51))
        self.button_validation.setText("VALIDER")
        font = QtGui.QFont()
        font.setPointSize(17)
        self.button_validation.setFont(font)
        #self.button_validation.setObjectName("pushButton")

        # Green LED light
        self.green_light = QtWidgets.QLabel(self.centralwidget)
        self.green_light.setGeometry(QtCore.QRect(473, 190, 35, 35))
        self.green_light.setEnabled(False)
        self.green_light.setText("")
        self.green_light.setPixmap(QtGui.QPixmap("./Files/led_green.png"))
        self.green_light.setScaledContents(True)
        #self.led_light.hide()
        #self.green_light.setObjectName("label")

        # Orange LED light
        self.orange_light = QtWidgets.QLabel(self.centralwidget)
        self.orange_light.setGeometry(QtCore.QRect(473, 190, 35, 35))
        self.orange_light.setEnabled(True)
        self.orange_light.setText("")
        self.orange_light.setPixmap(QtGui.QPixmap("./Files/led_orange.png"))
        self.orange_light.setScaledContents(True)
        self.orange_light.hide()
        #self.orange_light.setObjectName("label")

        # Label operator sign
        self.label_operator = QtWidgets.QLabel(self.centralwidget)
        self.label_operator.setGeometry(QtCore.QRect(120, 350, 21, 21))
        self.label_operator.setText(".")
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_operator.setFont(font)
        self.label_operator.setAlignment(QtCore.Qt.AlignCenter)
        #self.label_operator.setObjectName("label_5")

        # Vertical line
        self.v_line = QtWidgets.QFrame(self.centralwidget)
        self.v_line.setGeometry(QtCore.QRect(360, 260, 16, 261))
        self.v_line.setFrameShape(QtWidgets.QFrame.VLine)
        self.v_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        #self.v_line.setObjectName("line_2")

        # Button stop
        self.button_stop = QtWidgets.QPushButton(self.centralwidget)
        self.button_stop.setEnabled(False)
        self.button_stop.setText("STOP")
        self.button_stop.setGeometry(QtCore.QRect(470, 330, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.button_stop.setFont(font)
        #self.button_stop.setObjectName("pushButton_2")

        # Line edit
        self.onlyInt = QtGui.QIntValidator()
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(150, 340, 51, 41))
        self.lineEdit.setEnabled(False)
        self.lineEdit.setFont(font)
        self.lineEdit.setValidator(self.onlyInt)
        self.lineEdit.setMaxLength(3)
        #self.lineEdit.setObjectName("lineEdit")

        # LCD operation
        self.lcd_oper = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_oper.setGeometry(QtCore.QRect(30, 340, 81, 41))
        self.lcd_oper.setProperty("intValue", 0)
        #self.lcd_oper.setObjectName("lcdNumber")

        # LCD result
        self.lcd_res = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_res.setGeometry(QtCore.QRect(240, 340, 81, 41))
        self.lcd_res.setProperty("intValue", 0)
        #self.lcd_res.setObjectName("lcdNumber_2")

        # Label equal
        self.label_equal = QtWidgets.QLabel(self.centralwidget)
        self.label_equal.setGeometry(QtCore.QRect(210, 350, 21, 21))
        self.label_equal.setText("=")
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_equal.setFont(font)
        self.label_equal.setAlignment(QtCore.Qt.AlignCenter)
        #self.label_equal.setObjectName("label_6")

        # Label instruction
        self.label_instruc = QtWidgets.QLabel(self.centralwidget)
        self.label_instruc.setGeometry(QtCore.QRect(0, 260, 361, 31))
        self.label_instruc.setText("Résoudre cette équation pour désactiver l'alarme")
        font = QtGui.QFont()
        font.setFamily("Helonia")
        font.setPointSize(11)
        font.setItalic(True)
        self.label_instruc.setFont(font)
        self.label_instruc.setAlignment(QtCore.Qt.AlignCenter)
        #self.label_instruc.setObjectName("label_7")

        MainWindow.setCentralWidget(self.centralwidget)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())