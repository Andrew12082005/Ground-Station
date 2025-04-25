from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer ,QTime
import random
from src.gs import Ui_MainWindow
from src import decoder
from src import pic_rc


class MainApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_data)
        self.timer.start(100) 
    def inputdata(self):

        data = {
            "vx":decoder.vx,
            "vy":decoder.vy,
            "vz":decoder.vz,
            "ax":decoder.ax,
            "ay":decoder.ay,
            "az":decoder.az,
            "gx":decoder.gx,
            "gy":decoder.gy,
            "gz":decoder.gz,
            "fa":decoder.fa,
            "fv":decoder.fv,
            "fl":decoder.fl,
            "aoa": decoder.aoa,
            "ias": decoder.ias,
            "bat1": decoder.bat1,
            "bat2": decoder.bat2,
            "gpsla":decoder.gpsla,
            "gpslo":decoder.gpslo,
            "gpsal":decoder.gpsal,
            "Qxp":decoder.Qxp,
            "Qxn":decoder.Qxn,
            "Qyp":decoder.Qyp,
            "Qyn":decoder.Qyn,
            "Qm":decoder.Qm,
            "time": QTime.currentTime().toString()
        }
        return data
    def update_data(self):

        data = self.inputdata()
        self.ui.timevalue.setText(data["time"])
        self.ui.vxvalue.setText(f"{data['vx']:.2f}")
        self.ui.vyvalue.setText(f"{data['vy']:.2f}")
        self.ui.vzvalue.setText(f"{data['vz']:.2f}")
        self.ui.axvalue.setText(f"{data['ax']:.2f}")
        self.ui.ayvalue.setText(f"{data['ay']:.2f}")
        self.ui.azvalue.setText(f"{data['az']:.2f}")
        self.ui.gxvalue.setText(f"{data['gx']:.2f}")
        self.ui.gyvalue.setText(f"{data['gy']:.2f}")
        self.ui.gzvalue.setText(f"{data['gz']:.2f}")
        self.ui.attitudevalue.setText(f"{data['fa']:.2f}")
        self.ui.velocityvalue.setText(f"{data['fv']:.2f}")
        self.ui.loactionvalue.setText(f"{data['fl']:.2f}")
        self.ui.gpsaltitudevalue.setText(f"{data['gpsal']:.2f}")
        self.ui.latitudevalue.setText(f"{data['gpsla']:.2f}")
        self.ui.longitudevalue.setText(f"{data['gpslo']:.2f}")
        self.ui.aoavalue.setText(f"{data['aoa']:.2f}°")
        self.ui.iasvalue.setText(f"{data['ias']:.1f} m/s")
        self.ui.bat1value.setText(f"{data['bat1']:.2f} V")
        self.ui.bat2value.setText(f"{data['bat2']:.2f} V")
        self.ui.Qxp.setText(f"{data['Qxp']:.2f} kPa")
        self.ui.Qxn.setText(f"{data['Qxn']:.2f} kPa")
        self.ui.Qyp.setText(f"{data['Qyp']:.2f} kPa")
        self.ui.Qyn.setText(f"{data['Qyn']:.2f} kPa")
        self.ui.Qm.setText(f"{data['Qm']:.2f} kPa")
        self.ui.time.setText(data["time"])

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())
