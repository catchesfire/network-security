class SSC:

    def encrypt(self, lfsr_blocks, file_name, file_name_output):

        f = open(file_name, 'rb')
        f.seek(0, 2)
        file_size = f.tell()
        f2 = open(file_name_output, 'wb')
        counter = 0
        seek_counter = 1
        exitloop = False
        while 1:
            if exitloop:
                break
            y = []
            seek_value = seek_counter * -8192
            if seek_value < -file_size:
                temp_seek = f.tell() - 8192
                f.seek(0)
                if temp_seek > 0:
                    byte_s = f.read(temp_seek)
                else:
                    byte_s = f.read(file_size)

                exitloop = True

            else:
                f.seek(seek_value , 2)
                byte_s = f.read(8192)
            seek_counter +=1
            if not byte_s:
                break


            input = []
            #clean
            for j in range(len(byte_s) - 1 , -1, -1):
                if byte_s[j] != "\n" and byte_s[j] != "\r" and byte_s[j] != "\r\n":
                    input.append(byte_s[j])

            for j in range(len(input)):
                lfsr_elem = lfsr_blocks[counter % len(lfsr_blocks)]
                counter += 1

                y.append(((input[j] + int(lfsr_elem[0])) % 2).to_bytes(1, 'big'))

            for i in range(len(y)):
                f2.write(y[i])

        f.close()
        f2.close()

        return

    def decrypt(self, lfsr_blocks, file_name, file_name_output):

        f = open(file_name, 'rb')
        f2 = open('temp_file.bin', 'wb')
        counter = 0
        while 1:
            y = []

            byte_s = f.read(8192)
            if not byte_s:
                break

            input = []
            # reverse and clean
            for j in range(len(byte_s)):
                if byte_s[j] != "\n" and byte_s[j] != "\r" and byte_s[j] != "\r\n":
                    input.append(byte_s[j])

            for j in range(len(input)):
                lfsr_elem = lfsr_blocks[counter % len(lfsr_blocks)]
                counter += 1
                f2.write(((input[j] + int(lfsr_elem[0])) % 2).to_bytes(1, 'big'))

        f.close()
        f2.close()
        self.reverse_file('temp_file.bin', file_name_output)

        return

    def reverse_file(self, input_file, output_file):
            f = open(input_file, 'rb')
            f.seek(0, 2)
            file_size = f.tell()
            f2 = open(output_file, 'wb')
            counter = 0
            seek_counter = 1
            exitloop = False
            while 1:
                if exitloop:
                    break
                y = []
                seek_value = seek_counter * -8192
                if seek_value < -file_size:
                    temp_seek = f.tell() - 8192
                    f.seek(0)
                    if temp_seek > 0:
                        byte_s = f.read(temp_seek)
                    else:
                        byte_s = f.read(file_size)

                    exitloop = True

                else:
                    f.seek(seek_value, 2)
                    byte_s = f.read(8192)
                seek_counter += 1
                if not byte_s:
                    break

                for i in range(len(byte_s) -1, -1, -1):
                    f2.write(byte_s[i].to_bytes(1, 'big'))
            f.close()
            f2.close()