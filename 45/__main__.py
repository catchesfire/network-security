from LFSRGenerator import LFSR
from PyQt5.QtWidgets import QApplication
from views import LFSRView, MainView, SSCView
import sys

app = QApplication(sys.argv)
window = SSCView()
window.show()
sys.exit(app.exec_())
