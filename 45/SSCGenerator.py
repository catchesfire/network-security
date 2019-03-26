class SSC:

    def encrypt(self, lfsr_blocks, file_name, file_name_output):

        f = open(file_name, 'rb')
        f.seek(0, 2)
        file_size = f.tell()
        f2 = open(file_name_output, 'wb')
        counter = 0
        seek_counter = 1
        exitloop = False
        input2 = []
        while 1:
            if exitloop:
                break
            y = bytearray()
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
                    # input2.append("{:02x}".format(byte_s[j]))
                    input.append(byte_s[j])

            for j in range(len(input)):


                onne_str = "{:08b}".format(input[j])
                temp_byte = ""
                for k in range(8):
                    lfsr_elem = lfsr_blocks[counter % len(lfsr_blocks)]
                    if len(onne_str) > k:
                        counter += 1
                        result_xor = int(int(onne_str[k]) + int(lfsr_elem[0])) % 2
                        temp_byte += str(result_xor)

                int_byte = int(temp_byte, 2)

                y.append(int_byte)



                # y.append(((sum + int(lfsr_elem[0])) % 2).to_bytes(1, 'big'))

            for i in range(len(y)):
                f2.write(y[i].to_bytes(1, 'big'))

        f.close()
        f2.close()

        return

    def decrypt(self, lfsr_blocks, file_name, file_name_output):

        f = open(file_name, 'rb')
        f2 = open('temp_file.bin', 'wb')
        counter = 0
        while 1:
            y = bytearray()

            byte_s = f.read(8192)
            if not byte_s:
                break

            input = []
            # reverse and clean
            for j in range(len(byte_s)):
                if byte_s[j] != "\n" and byte_s[j] != "\r" and byte_s[j] != "\r\n":

                    input.append(byte_s[j])

            for j in range(len(input)):

                onne_str = "{:08b}".format(input[j])
                temp_byte = ""

                for k in range(8):
                    lfsr_elem = lfsr_blocks[counter % len(lfsr_blocks)]
                    if len(onne_str) > k:
                        counter += 1
                        result_xor = int(int(onne_str[k]) + int(lfsr_elem[0])) % 2
                        temp_byte += str(result_xor)

                int_byte = int(temp_byte, 2)
                y.append(int_byte)

            for i in range(len(y)):
                f2.write(y[i].to_bytes(1, 'big'))


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

from PyQt5.QtWidgets import QApplication
import views
import sys

if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = views.SSCView()
    window.show()
    sys.exit(app.exec_())