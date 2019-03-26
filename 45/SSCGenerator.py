class SSC:

    def encrypt_n_decrypt(self, lfsr_blocks, file_name, file_name_output):

        f = open(file_name, 'rb')
        f2 = open(file_name_output, 'wb')
        counter = 0
        while 1:
            y = []
            byte_s = f.read(8192)
            if not byte_s:
                break

            for j in range(len(byte_s) - 1, -1, -1):
                lfsr_elem = lfsr_blocks[counter % len(lfsr_blocks)]
                counter += 1
                y.append(((byte_s[j] + int(lfsr_elem[0])) % 2).to_bytes(1, 'big'))

            #print("out sscgenerator: ", y)
            for i in range(len(y)):
                f2.write(y[i])

        f.close()
        f2.close()

        return




