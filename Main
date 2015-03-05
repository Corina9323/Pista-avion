import sys
from PyQt4.QtGui import QApplication, QWidget
from radar import Ui_RadarWidget
import ModelImpl
from math import trunc

from Simul1 import Simul1
from threading import Thread
from Simul2 import Simul2
app = QApplication(sys.argv)
window = QWidget()
ui = Simul2(10, 1000, 4)
ui.setupUi(window)

datain=[]
#sim=Simulation(10, 1, 4)
ui.setGraphicalModel()
#thread = Thread(target = ui.startInit)
#thread.start()
app.aboutToQuit.connect(ui.stopInit)
window.show()
sys.exit(app.exec_())
