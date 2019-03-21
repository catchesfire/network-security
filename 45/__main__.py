from LFSRGenerator import LFSR
from PyQt5.QtWidgets import QApplication
from views import LFSRView
import sys

app = QApplication(sys.argv)
window = LFSRView()
sys.exit(app.exec_())