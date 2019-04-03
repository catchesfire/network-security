class DES:

    def __init__(self, source_file_name, destination_file_name):
        self.source_file_name = source_file_name
        self.destination_file_name = destination_file_name

    def hex_to_binary(self, hex_byte_array):
        binary_array = []
        for hex_byte in hex_byte_array:
            binary_array.append("{:08b}".format(hex_byte))

        return binary_array

    def binary_to_hex(self, binary_array):
        hex_array = bytearray()
        for binary_byte in binary_array:
            hex_array.append(int(binary_byte, 2))

        return hex_array

    def run(self):
        with open(self.source_file_name, "rb") as source_file, open(self.destination_file_name, "wb") as destination_file:
            while 1:
                byte_s = source_file.read(32768)

                if not byte_s:
                    break

                binary_source_block = self.hex_to_binary(byte_s)
                binary_destination_block = []

                for i in range(0, len(binary_source_block), 8):
                    input_64_bit = "".join(binary_source_block[i:i+8])
                    output_64_bit = input_64_bit # wynik funkcji enkryptujacej (des) do zapisania do pliku 
                    for j in range(8):
                        binary_destination_block.append(output_64_bit[j*8:j*8+8])
                
                byte_output = self.binary_to_hex(binary_destination_block)

                for byte in byte_output:
                    destination_file.write(byte.to_bytes(1, "big"))




if __name__ == "__main__":
    des = DES("68/test.bin", "68/out.bin")
    des.run()