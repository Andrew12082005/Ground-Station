# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gs.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from src import pic_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(1840, 1095)
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(20)
        MainWindow.setFont(font)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.gpsbox = QtWidgets.QGroupBox(self.tab)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        self.gpsbox.setFont(font)
        self.gpsbox.setStyleSheet("color:black;")
        self.gpsbox.setObjectName("gpsbox")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.gpsbox)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.latitudevalue = QtWidgets.QLabel(self.gpsbox)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        self.latitudevalue.setFont(font)
        self.latitudevalue.setStyleSheet("color:black;background-color:white;")
        self.latitudevalue.setText("")
        self.latitudevalue.setObjectName("latitudevalue")
        self.gridLayout_9.addWidget(self.latitudevalue, 1, 0, 1, 1)
        self.longitudevalue = QtWidgets.QLabel(self.gpsbox)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        self.longitudevalue.setFont(font)
        self.longitudevalue.setStyleSheet("color:black;background-color:white;")
        self.longitudevalue.setText("")
        self.longitudevalue.setObjectName("longitudevalue")
        self.gridLayout_9.addWidget(self.longitudevalue, 1, 1, 1, 1)
        self.gpsaltitude = QtWidgets.QLabel(self.gpsbox)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        self.gpsaltitude.setFont(font)
        self.gpsaltitude.setStyleSheet("color:black;")
        self.gpsaltitude.setObjectName("gpsaltitude")
        self.gridLayout_9.addWidget(self.gpsaltitude, 0, 2, 1, 1)
        self.gpsaltitudevalue = QtWidgets.QLabel(self.gpsbox)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        self.gpsaltitudevalue.setFont(font)
        self.gpsaltitudevalue.setStyleSheet("color:black;background-color:white;")
        self.gpsaltitudevalue.setText("")
        self.gpsaltitudevalue.setObjectName("gpsaltitudevalue")
        self.gridLayout_9.addWidget(self.gpsaltitudevalue, 1, 2, 1, 1)
        self.latitude = QtWidgets.QLabel(self.gpsbox)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        self.latitude.setFont(font)
        self.latitude.setStyleSheet("color:black;")
        self.latitude.setObjectName("latitude")
        self.gridLayout_9.addWidget(self.latitude, 0, 0, 1, 1)
        self.longitude = QtWidgets.QLabel(self.gpsbox)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        self.longitude.setFont(font)
        self.longitude.setStyleSheet("color:black;")
        self.longitude.setObjectName("longitude")
        self.gridLayout_9.addWidget(self.longitude, 0, 1, 1, 1)
        self.gridLayout_11.addWidget(self.gpsbox, 6, 1, 1, 1)
        self.gyro = QtWidgets.QGroupBox(self.tab)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.gyro.setFont(font)
        self.gyro.setObjectName("gyro")
        self.gridLayout = QtWidgets.QGridLayout(self.gyro)
        self.gridLayout.setObjectName("gridLayout")
        self.gx = QtWidgets.QLabel(self.gyro)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.gx.setFont(font)
        self.gx.setObjectName("gx")
        self.gridLayout.addWidget(self.gx, 0, 1, 1, 1)
        self.gy = QtWidgets.QLabel(self.gyro)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.gy.setFont(font)
        self.gy.setObjectName("gy")
        self.gridLayout.addWidget(self.gy, 0, 2, 1, 1)
        self.gz = QtWidgets.QLabel(self.gyro)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.gz.setFont(font)
        self.gz.setObjectName("gz")
        self.gridLayout.addWidget(self.gz, 0, 3, 1, 1)
        self.gzvalue = QtWidgets.QLabel(self.gyro)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        self.gzvalue.setFont(font)
        self.gzvalue.setStyleSheet("background-color:white")
        self.gzvalue.setText("")
        self.gzvalue.setObjectName("gzvalue")
        self.gridLayout.addWidget(self.gzvalue, 1, 3, 1, 1)
        self.gyvalue = QtWidgets.QLabel(self.gyro)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        self.gyvalue.setFont(font)
        self.gyvalue.setStyleSheet("background-color:white")
        self.gyvalue.setText("")
        self.gyvalue.setObjectName("gyvalue")
        self.gridLayout.addWidget(self.gyvalue, 1, 2, 1, 1)
        self.gxvalue = QtWidgets.QLabel(self.gyro)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        self.gxvalue.setFont(font)
        self.gxvalue.setStyleSheet("background-color:white")
        self.gxvalue.setText("")
        self.gxvalue.setObjectName("gxvalue")
        self.gridLayout.addWidget(self.gxvalue, 1, 1, 1, 1)
        self.gridLayout_11.addWidget(self.gyro, 6, 2, 1, 1)
        self.payloadbox = QtWidgets.QGroupBox(self.tab)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        self.payloadbox.setFont(font)
        self.payloadbox.setStyleSheet("color:black;")
        self.payloadbox.setObjectName("payloadbox")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.payloadbox)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.aoa = QtWidgets.QLabel(self.payloadbox)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        self.aoa.setFont(font)
        self.aoa.setStyleSheet("color:black;")
        self.aoa.setObjectName("aoa")
        self.gridLayout_7.addWidget(self.aoa, 0, 1, 1, 1)
        self.aoavalue = QtWidgets.QLabel(self.payloadbox)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        self.aoavalue.setFont(font)
        self.aoavalue.setStyleSheet("color:black;background-color:white;")
        self.aoavalue.setText("")
        self.aoavalue.setObjectName("aoavalue")
        self.gridLayout_7.addWidget(self.aoavalue, 1, 1, 1, 1)
        self.iasvalue = QtWidgets.QLabel(self.payloadbox)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        self.iasvalue.setFont(font)
        self.iasvalue.setStyleSheet("color:black;background-color:white;")
        self.iasvalue.setText("")
        self.iasvalue.setObjectName("iasvalue")
        self.gridLayout_7.addWidget(self.iasvalue, 1, 0, 1, 1)
        self.ias = QtWidgets.QLabel(self.payloadbox)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        self.ias.setFont(font)
        self.ias.setStyleSheet("color:black;")
        self.ias.setObjectName("ias")
        self.gridLayout_7.addWidget(self.ias, 0, 0, 1, 1)
        self.gridLayout_11.addWidget(self.payloadbox, 8, 1, 1, 1)
        self.line = QtWidgets.QFrame(self.tab)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(9)
        self.line.setFont(font)
        self.line.setStyleSheet("color:black;")
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(200)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.gridLayout_11.addWidget(self.line, 1, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(553, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_11.addItem(spacerItem, 0, 1, 1, 1)
        self.epsbox = QtWidgets.QGroupBox(self.tab)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        self.epsbox.setFont(font)
        self.epsbox.setStyleSheet("color:black;")
        self.epsbox.setObjectName("epsbox")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.epsbox)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.bat2 = QtWidgets.QLabel(self.epsbox)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        self.bat2.setFont(font)
        self.bat2.setStyleSheet("color:black;")
        self.bat2.setObjectName("bat2")
        self.gridLayout_8.addWidget(self.bat2, 0, 1, 1, 1)
        self.bat1value = QtWidgets.QLabel(self.epsbox)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        self.bat1value.setFont(font)
        self.bat1value.setStyleSheet("color:black;background-color:white;")
        self.bat1value.setText("")
        self.bat1value.setObjectName("bat1value")
        self.gridLayout_8.addWidget(self.bat1value, 1, 0, 1, 1)
        self.bat1 = QtWidgets.QLabel(self.epsbox)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        self.bat1.setFont(font)
        self.bat1.setStyleSheet("color:black;")
        self.bat1.setObjectName("bat1")
        self.gridLayout_8.addWidget(self.bat1, 0, 0, 1, 1)
        self.bat2value = QtWidgets.QLabel(self.epsbox)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        self.bat2value.setFont(font)
        self.bat2value.setStyleSheet("color:black;background-color:white;")
        self.bat2value.setText("")
        self.bat2value.setObjectName("bat2value")
        self.gridLayout_8.addWidget(self.bat2value, 1, 1, 1, 1)
        self.gridLayout_11.addWidget(self.epsbox, 8, 2, 1, 1)
        self.accleration = QtWidgets.QGroupBox(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.accleration.sizePolicy().hasHeightForWidth())
        self.accleration.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.accleration.setFont(font)
        self.accleration.setObjectName("accleration")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.accleration)
        self.gridLayout_2.setHorizontalSpacing(7)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.ayvalue = QtWidgets.QLabel(self.accleration)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.ayvalue.setFont(font)
        self.ayvalue.setStyleSheet("background-color:white;")
        self.ayvalue.setText("")
        self.ayvalue.setObjectName("ayvalue")
        self.gridLayout_2.addWidget(self.ayvalue, 1, 1, 1, 1)
        self.az = QtWidgets.QLabel(self.accleration)
        self.az.setObjectName("az")
        self.gridLayout_2.addWidget(self.az, 0, 2, 1, 1)
        self.axvalue = QtWidgets.QLabel(self.accleration)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.axvalue.setFont(font)
        self.axvalue.setStyleSheet("background-color:white;")
        self.axvalue.setText("")
        self.axvalue.setObjectName("axvalue")
        self.gridLayout_2.addWidget(self.axvalue, 1, 0, 1, 1)
        self.azvalue = QtWidgets.QLabel(self.accleration)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.azvalue.setFont(font)
        self.azvalue.setStyleSheet("background-color:white;")
        self.azvalue.setText("")
        self.azvalue.setObjectName("azvalue")
        self.gridLayout_2.addWidget(self.azvalue, 1, 2, 1, 1)
        self.ax = QtWidgets.QLabel(self.accleration)
        self.ax.setObjectName("ax")
        self.gridLayout_2.addWidget(self.ax, 0, 0, 1, 1)
        self.ay = QtWidgets.QLabel(self.accleration)
        self.ay.setObjectName("ay")
        self.gridLayout_2.addWidget(self.ay, 0, 1, 1, 1)
        self.gridLayout_11.addWidget(self.accleration, 4, 2, 1, 1)
        self.velocitybox = QtWidgets.QGroupBox(self.tab)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        self.velocitybox.setFont(font)
        self.velocitybox.setStyleSheet("color:black;")
        self.velocitybox.setObjectName("velocitybox")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.velocitybox)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.vxvalue = QtWidgets.QLabel(self.velocitybox)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        self.vxvalue.setFont(font)
        self.vxvalue.setAutoFillBackground(False)
        self.vxvalue.setStyleSheet("color:black;background-color:white;")
        self.vxvalue.setText("")
        self.vxvalue.setObjectName("vxvalue")
        self.gridLayout_6.addWidget(self.vxvalue, 1, 0, 1, 1)
        self.vz = QtWidgets.QLabel(self.velocitybox)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        self.vz.setFont(font)
        self.vz.setStyleSheet("color:black;")
        self.vz.setObjectName("vz")
        self.gridLayout_6.addWidget(self.vz, 0, 2, 1, 1)
        self.vzvalue = QtWidgets.QLabel(self.velocitybox)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        self.vzvalue.setFont(font)
        self.vzvalue.setStyleSheet("color:black;background-color:white;")
        self.vzvalue.setText("")
        self.vzvalue.setObjectName("vzvalue")
        self.gridLayout_6.addWidget(self.vzvalue, 1, 2, 1, 1)
        self.vx = QtWidgets.QLabel(self.velocitybox)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        self.vx.setFont(font)
        self.vx.setStyleSheet("color:black;")
        self.vx.setObjectName("vx")
        self.gridLayout_6.addWidget(self.vx, 0, 0, 1, 1)
        self.vyvalue = QtWidgets.QLabel(self.velocitybox)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        self.vyvalue.setFont(font)
        self.vyvalue.setStyleSheet("color:black;background-color:white;")
        self.vyvalue.setText("")
        self.vyvalue.setObjectName("vyvalue")
        self.gridLayout_6.addWidget(self.vyvalue, 1, 1, 1, 1)
        self.vy = QtWidgets.QLabel(self.velocitybox)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        self.vy.setFont(font)
        self.vy.setStyleSheet("color:black;")
        self.vy.setObjectName("vy")
        self.gridLayout_6.addWidget(self.vy, 0, 1, 1, 1)
        self.gridLayout_11.addWidget(self.velocitybox, 2, 2, 1, 1)
        self.checklist = QtWidgets.QGroupBox(self.tab)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.checklist.setFont(font)
        self.checklist.setObjectName("checklist")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.checklist)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.com = QtWidgets.QLabel(self.checklist)
        self.com.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        self.com.setFont(font)
        self.com.setStyleSheet("color:black;")
        self.com.setObjectName("com")
        self.gridLayout_13.addWidget(self.com, 0, 1, 1, 1)
        self.checkAvonics = QtWidgets.QCheckBox(self.checklist)
        self.checkAvonics.setObjectName("checkAvonics")
        self.gridLayout_13.addWidget(self.checkAvonics, 2, 2, 1, 1)
        self.connect = QtWidgets.QPushButton(self.checklist)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        self.connect.setFont(font)
        self.connect.setObjectName("connect")
        self.gridLayout_13.addWidget(self.connect, 0, 3, 1, 1)
        self.comport = QtWidgets.QComboBox(self.checklist)
        self.comport.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        self.comport.setFont(font)
        self.comport.setStyleSheet("color:black;")
        self.comport.setEditable(False)
        self.comport.setInsertPolicy(QtWidgets.QComboBox.InsertAtCurrent)
        self.comport.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLengthWithIcon)
        self.comport.setDuplicatesEnabled(False)
        self.comport.setFrame(False)
        self.comport.setModelColumn(0)
        self.comport.setObjectName("comport")
        self.comport.addItem("")
        self.comport.addItem("")
        self.gridLayout_13.addWidget(self.comport, 0, 2, 1, 1)
        self.statusavonics = QtWidgets.QLabel(self.checklist)
        self.statusavonics.setText("")
        self.statusavonics.setPixmap(QtGui.QPixmap(":/newPrefix/STANDBY.png"))
        self.statusavonics.setObjectName("statusavonics")
        self.gridLayout_13.addWidget(self.statusavonics, 2, 1, 1, 1)
        self.gridLayout_11.addWidget(self.checklist, 2, 0, 3, 1)
        self.widget = QtWidgets.QWidget(self.tab)
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setStyleSheet("color:black;")
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.frame = QtWidgets.QFrame(self.widget)
        self.frame.setMinimumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.frame.setFont(font)
        self.frame.setStyleSheet("image: url(:/newPrefix/raw.png);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2.addWidget(self.frame)
        self.gridLayout_11.addWidget(self.widget, 0, 2, 1, 1)
        self.TIME = QtWidgets.QWidget(self.tab)
        self.TIME.setObjectName("TIME")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.TIME)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.timelabel = QtWidgets.QLabel(self.TIME)
        self.timelabel.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(30)
        self.timelabel.setFont(font)
        self.timelabel.setStyleSheet("")
        self.timelabel.setScaledContents(True)
        self.timelabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.timelabel.setObjectName("timelabel")
        self.horizontalLayout.addWidget(self.timelabel)
        self.ctime = QtWidgets.QLabel(self.TIME)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.ctime.setFont(font)
        self.ctime.setObjectName("ctime")
        self.horizontalLayout.addWidget(self.ctime)
        self.gridLayout_11.addWidget(self.TIME, 0, 0, 1, 1)
        self.flighttimebox = QtWidgets.QGroupBox(self.tab)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        self.flighttimebox.setFont(font)
        self.flighttimebox.setObjectName("flighttimebox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.flighttimebox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.timevalue = QtWidgets.QLabel(self.flighttimebox)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        self.timevalue.setFont(font)
        self.timevalue.setStyleSheet("background-color:white;")
        self.timevalue.setObjectName("timevalue")
        self.gridLayout_4.addWidget(self.timevalue, 1, 0, 1, 1)
        self.launchbutton = QtWidgets.QPushButton(self.flighttimebox)
        self.launchbutton.setObjectName("launchbutton")
        self.gridLayout_4.addWidget(self.launchbutton, 1, 1, 1, 1)
        self.gridLayout_11.addWidget(self.flighttimebox, 2, 1, 1, 1)
        self.flightdata = QtWidgets.QGroupBox(self.tab)
        self.flightdata.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        self.flightdata.setFont(font)
        self.flightdata.setStyleSheet("color:black;")
        self.flightdata.setObjectName("flightdata")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.flightdata)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.attitudevalue = QtWidgets.QLabel(self.flightdata)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        self.attitudevalue.setFont(font)
        self.attitudevalue.setStyleSheet("color:black;background-color:white;")
        self.attitudevalue.setText("")
        self.attitudevalue.setObjectName("attitudevalue")
        self.gridLayout_5.addWidget(self.attitudevalue, 1, 0, 1, 1)
        self.velocityvalue = QtWidgets.QLabel(self.flightdata)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        self.velocityvalue.setFont(font)
        self.velocityvalue.setStyleSheet("color:black;background-color:white;")
        self.velocityvalue.setText("")
        self.velocityvalue.setObjectName("velocityvalue")
        self.gridLayout_5.addWidget(self.velocityvalue, 1, 1, 1, 1)
        self.velocity = QtWidgets.QLabel(self.flightdata)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        self.velocity.setFont(font)
        self.velocity.setStyleSheet("color:black;")
        self.velocity.setObjectName("velocity")
        self.gridLayout_5.addWidget(self.velocity, 0, 1, 1, 1)
        self.altitude = QtWidgets.QLabel(self.flightdata)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        self.altitude.setFont(font)
        self.altitude.setStyleSheet("color:black;")
        self.altitude.setObjectName("altitude")
        self.gridLayout_5.addWidget(self.altitude, 0, 0, 1, 1)
        self.location = QtWidgets.QLabel(self.flightdata)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        self.location.setFont(font)
        self.location.setStyleSheet("color:black;")
        self.location.setObjectName("location")
        self.gridLayout_5.addWidget(self.location, 0, 2, 1, 1)
        self.loactionvalue = QtWidgets.QLabel(self.flightdata)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        self.loactionvalue.setFont(font)
        self.loactionvalue.setStyleSheet("color:black;background-color:white;")
        self.loactionvalue.setText("")
        self.loactionvalue.setObjectName("loactionvalue")
        self.gridLayout_5.addWidget(self.loactionvalue, 1, 2, 1, 1)
        self.gridLayout_11.addWidget(self.flightdata, 4, 1, 1, 1)
        self.AoAVane = QtWidgets.QGroupBox(self.tab)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.AoAVane.setFont(font)
        self.AoAVane.setObjectName("AoAVane")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.AoAVane)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.XN = QtWidgets.QLabel(self.AoAVane)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        self.XN.setFont(font)
        self.XN.setObjectName("XN")
        self.gridLayout_3.addWidget(self.XN, 0, 1, 1, 1)
        self.XP = QtWidgets.QLabel(self.AoAVane)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        self.XP.setFont(font)
        self.XP.setObjectName("XP")
        self.gridLayout_3.addWidget(self.XP, 0, 0, 1, 1)
        self.YN = QtWidgets.QLabel(self.AoAVane)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        self.YN.setFont(font)
        self.YN.setObjectName("YN")
        self.gridLayout_3.addWidget(self.YN, 0, 3, 1, 1)
        self.XPV = QtWidgets.QLabel(self.AoAVane)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        self.XPV.setFont(font)
        self.XPV.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.XPV.setObjectName("XPV")
        self.gridLayout_3.addWidget(self.XPV, 1, 0, 1, 1)
        self.XNV = QtWidgets.QLabel(self.AoAVane)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        self.XNV.setFont(font)
        self.XNV.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.XNV.setObjectName("XNV")
        self.gridLayout_3.addWidget(self.XNV, 1, 1, 1, 1)
        self.YNV = QtWidgets.QLabel(self.AoAVane)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        self.YNV.setFont(font)
        self.YNV.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.YNV.setObjectName("YNV")
        self.gridLayout_3.addWidget(self.YNV, 1, 3, 1, 1)
        self.YPV = QtWidgets.QLabel(self.AoAVane)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        self.YPV.setFont(font)
        self.YPV.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.YPV.setObjectName("YPV")
        self.gridLayout_3.addWidget(self.YPV, 1, 2, 1, 1)
        self.YP = QtWidgets.QLabel(self.AoAVane)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        self.YP.setFont(font)
        self.YP.setObjectName("YP")
        self.gridLayout_3.addWidget(self.YP, 0, 2, 1, 1)
        self.gridLayout_11.addWidget(self.AoAVane, 9, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_11.addItem(spacerItem1, 9, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_11.addItem(spacerItem2, 11, 2, 1, 1)
        self.Qball = QtWidgets.QGroupBox(self.tab)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        self.Qball.setFont(font)
        self.Qball.setAutoFillBackground(False)
        self.Qball.setStyleSheet("")
        self.Qball.setObjectName("Qball")
        self.bg = QtWidgets.QLabel(self.Qball)
        self.bg.setGeometry(QtCore.QRect(20, 40, 591, 341))
        self.bg.setStyleSheet("image: url(:/newPrefix/Qball.drawio.png);")
        self.bg.setText("")
        self.bg.setObjectName("bg")
        self.Qxp = QtWidgets.QLabel(self.Qball)
        self.Qxp.setGeometry(QtCore.QRect(40, 90, 131, 41))
        self.Qxp.setObjectName("Qxp")
        self.Qyn = QtWidgets.QLabel(self.Qball)
        self.Qyn.setGeometry(QtCore.QRect(40, 180, 131, 41))
        self.Qyn.setObjectName("Qyn")
        self.Qxn = QtWidgets.QLabel(self.Qball)
        self.Qxn.setGeometry(QtCore.QRect(40, 300, 131, 41))
        self.Qxn.setObjectName("Qxn")
        self.Qm = QtWidgets.QLabel(self.Qball)
        self.Qm.setGeometry(QtCore.QRect(490, 80, 131, 41))
        self.Qm.setObjectName("Qm")
        self.Qyp = QtWidgets.QLabel(self.Qball)
        self.Qyp.setGeometry(QtCore.QRect(490, 270, 131, 41))
        self.Qyp.setObjectName("Qyp")
        self.gridLayout_11.addWidget(self.Qball, 6, 0, 5, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout_10.addWidget(self.tabWidget, 0, 0, 3, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.comport.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.gpsbox.setTitle(_translate("MainWindow", "GPS"))
        self.gpsaltitude.setText(_translate("MainWindow", "Altitude"))
        self.latitude.setText(_translate("MainWindow", "Latitude"))
        self.longitude.setText(_translate("MainWindow", "Longitude"))
        self.gyro.setTitle(_translate("MainWindow", "Gyroscope"))
        self.gx.setText(_translate("MainWindow", "X"))
        self.gy.setText(_translate("MainWindow", "Y"))
        self.gz.setText(_translate("MainWindow", "Z"))
        self.payloadbox.setTitle(_translate("MainWindow", "Payload"))
        self.aoa.setText(_translate("MainWindow", "AoA"))
        self.ias.setText(_translate("MainWindow", "IAS"))
        self.epsbox.setTitle(_translate("MainWindow", "EPS"))
        self.bat2.setText(_translate("MainWindow", "BAT 2"))
        self.bat1.setText(_translate("MainWindow", "BAT 1"))
        self.accleration.setTitle(_translate("MainWindow", "Accleration"))
        self.az.setText(_translate("MainWindow", "az"))
        self.ax.setText(_translate("MainWindow", "ax"))
        self.ay.setText(_translate("MainWindow", "ay"))
        self.velocitybox.setTitle(_translate("MainWindow", "Velocity"))
        self.vz.setText(_translate("MainWindow", "Vz"))
        self.vx.setText(_translate("MainWindow", "Vx"))
        self.vy.setText(_translate("MainWindow", "Vy"))
        self.checklist.setTitle(_translate("MainWindow", "Checklist"))
        self.com.setText(_translate("MainWindow", "COM Port"))
        self.checkAvonics.setText(_translate("MainWindow", "Avionic"))
        self.connect.setText(_translate("MainWindow", "Connect"))
        self.comport.setCurrentText(_translate("MainWindow", "COM3"))
        self.comport.setItemText(0, _translate("MainWindow", "COM3"))
        self.comport.setItemText(1, _translate("MainWindow", "COM5"))
        self.label.setText(_translate("MainWindow", "STAR KILAKILA Mission Control Panel"))
        self.timelabel.setText(_translate("MainWindow", "Current Time"))
        self.ctime.setText(_translate("MainWindow", "TextLabel"))
        self.flighttimebox.setTitle(_translate("MainWindow", "Flight Time"))
        self.timevalue.setText(_translate("MainWindow", "TextLabel"))
        self.launchbutton.setText(_translate("MainWindow", "Launch"))
        self.flightdata.setTitle(_translate("MainWindow", "Flight Data"))
        self.velocity.setText(_translate("MainWindow", "Velocity"))
        self.altitude.setText(_translate("MainWindow", "Altitude"))
        self.location.setText(_translate("MainWindow", "Location"))
        self.AoAVane.setTitle(_translate("MainWindow", "AoA Vane"))
        self.XN.setText(_translate("MainWindow", "X Negative"))
        self.XP.setText(_translate("MainWindow", "X Positive"))
        self.YN.setText(_translate("MainWindow", "Y Negative"))
        self.XPV.setText(_translate("MainWindow", "TextLabel"))
        self.XNV.setText(_translate("MainWindow", "TextLabel"))
        self.YNV.setText(_translate("MainWindow", "TextLabel"))
        self.YPV.setText(_translate("MainWindow", "TextLabel"))
        self.YP.setText(_translate("MainWindow", "Y Positive"))
        self.Qball.setTitle(_translate("MainWindow", "QBall"))
        self.Qxp.setText(_translate("MainWindow", "TextLabel"))
        self.Qyn.setText(_translate("MainWindow", "TextLabel"))
        self.Qxn.setText(_translate("MainWindow", "TextLabel"))
        self.Qm.setText(_translate("MainWindow", "TextLabel"))
        self.Qyp.setText(_translate("MainWindow", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Flight Data"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Map"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
