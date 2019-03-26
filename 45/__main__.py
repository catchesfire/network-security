from LFSRGenerator import LFSR
# from SSCGenerator import SSC
# from CAutokey import CAutokey
#
# lfsr = LFSR()
# lfsr_blocks = lfsr.generate_blocks("1001", "1101")
# #print(lfsr_blocks)
#
# #
# # ssc = SSC()
# # encrypted = ssc.encrypt(lfsr_blocks, 'test.bin', 'out.bin')
# # decrypted = ssc.decrypt(lfsr_blocks, 'out.bin', 'test1.bin')
# #
# #
# cauto = CAutokey()
# encrypted = cauto.encrypt("1001", "1101",'test.bin', 'out.bin')
# decrypted = cauto.decrypt("1001", "1101",'out.bin', 'test11.bin')
from PyQt5.QtWidgets import QApplication
from views import CAutoKeyView, LFSRView, MainView, SSCView
import sys

app = QApplication(sys.argv)
# window = LFSRView()
#window = CAutoKeyView()
# window = SSCView()
window = MainView()
window.show()
sys.exit(app.exec_())
