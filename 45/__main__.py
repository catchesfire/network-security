from LFSRGenerator import LFSR
from SSCGenerator import SSC
# from CAutokey import CAutokey

lfsr = LFSR()
lfsr_blocks = lfsr.generate_blocks("1001", "1101")
#print(lfsr_blocks)

#
ssc = SSC()
encrypted = ssc.encrypt(lfsr_blocks, 'test2.bin', 'out.bin')
decrypted = ssc.decrypt(lfsr_blocks, 'out.bin', 'test21.bin')
#
#
# cauto = CAutokey()
# encrypted = cauto.encrypt("1001", "1101","aa", "bb")
# decrypted = cauto.decrypt("1001", "1101","aa", "bb")

