class CAutokey:

    def encrypt(self, polynomial, seed, file_name, file_name_output):
        c = polynomial
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
            y_out = bytearray()

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

            input = []
            # clean
            for j in range(len(byte_s) - 1, -1, -1):
                if byte_s[j] != "\n" and byte_s[j] != "\r" and byte_s[j] != "\r\n":
                    input.append(byte_s[j])


            reg = seed

            for i in range(len(input)):
                onne_str = "{:08b}".format(input[i])
                temp_byte = ""
                for k in range(8):

                    y = 0
                    # y to wynik xora skladnikow wieloianu (wewnetrzny xor)
                    for j in range(len(polynomial)):
                        if c[j] == '1':
                            y += int(reg[j])
                    # dodajemy skladnik x i xorujemy
                    y = int(y + int(onne_str[k])) % 2
                    temp_byte += str(y)

                    tmp = str(y)
                    #zatrzasniecie nowego stanu
                    for j in range(len(reg) -1):
                        tmp += reg[j]
                    reg = tmp

                #save y

                int_byte = int(temp_byte, 2)
                y_out.append(int_byte)
                # f2.write(y.to_bytes(1, 'big'))
            for i in range(len(y_out)):
                f2.write(y_out[i].to_bytes(1, 'big'))



    def decrypt(self, polynomial, seed, file_name, file_name_output):
        c = polynomial

        f = open(file_name, 'rb')
        f2 = open('temp_file.bin', 'wb')
        counter = 0
        while 1:
            y = []
            y_out = bytearray()

            byte_s = f.read(8192)
            if not byte_s:
                break

            input = []
            # reverse and clean
            for j in range(len(byte_s)):
                if byte_s[j] != "\n" and byte_s[j] != "\r" and byte_s[j] != "\r\n":
                    input.append(byte_s[j])


            reg = seed
            for i in range(len(input)):
                onne_str = "{:08b}".format(input[i])
                temp_byte = ""
                for k in range(8):

                    y = 0
                    # y to wynik xora skladnikow wieloianu (wewnetrzny xor)
                    for j in range(len(polynomial)):
                        if c[j] == '1':
                            y += int(reg[j])
                    # dodajemy skladnik x i xorujemy
                    y = int(y + int(onne_str[k])) % 2
                    temp_byte += str(y)

                    tmp = str(onne_str[k])
                    #zatrzasniecie nowego stanu
                    for j in range(len(reg) -1):
                        tmp += reg[j]
                    reg = tmp

                #save y
                # f2.write(y.to_bytes(1, 'big'))
                int_byte = int(temp_byte, 2)
                y_out.append(int_byte)
                # f2.write(y.to_bytes(1, 'big'))
            for i in range(len(y_out)):
                f2.write(y_out[i].to_bytes(1, 'big'))


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
    window = views.CAutokeyView()
    window.show()
    sys.exit(app.exec_())