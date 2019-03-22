from LFSRGenerator import LFSR
from SSCGenerator import SSC

lfsr = LFSR()
lfsr_blocks = lfsr.generate_blocks("1001", "1101")
#print(lfsr_blocks)


ssc = SSC()
encrypted = ssc.encrypt_n_decrypt(lfsr_blocks, 'test.bin', 'out.bin')
# print(encrypted)


