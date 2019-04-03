class DES:
    PC1 = [57, 49, 41, 33, 25, 17, 9,
           1, 58, 50, 42, 34, 26, 18,
           10, 2, 59, 51, 43, 35, 27,
           19, 11, 3, 60, 52, 44, 36,
           63, 55, 47, 39, 31, 23, 15,
           7, 62, 54, 46, 38, 30, 22,
           14, 6, 61, 53, 45, 37, 29,
           21, 13, 5, 28, 20, 12, 4]

    PC2 = [14, 17, 11, 24, 1, 5,
           3, 28, 15, 6, 21, 10,
           23, 19, 12, 4, 26, 8,
           16, 7, 27, 20, 13, 2,
           41, 52, 31, 37, 47, 55,
           30, 40, 51, 45, 33, 48,
           44, 49, 39, 56, 34, 53,
           46, 42, 50, 36, 29, 32]

    LSHIFT_MAP = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

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

    def generate_subkeys(self, hex_key):
        subkeys = []
        binnary_key = ""
        for char in hex_key:
            binnary_char = "{:04b}".format(int(char, 16))
            binnary_key += binnary_char

        key = self.permutate(binnary_key, self.PC1)

        for i in range(16):

            left_half = key[:28]
            right_half = key[28:]
            left_half = self.left_shift(left_half, self.LSHIFT_MAP[i])
            right_half = self.left_shift(right_half, self.LSHIFT_MAP[i])
            key = left_half + right_half
            subkey = self.permutate(key, self.PC2)
            subkeys.append(subkey)

    def left_shift(self, input, shift_val):
        shifted = input[shift_val:]
        for i in range(shift_val):
            shifted += "0"
        return shifted

    def permutate(self, source, permutation_order):
        out = ""
        for order in permutation_order:
            out += source[order-1]
        return out


if __name__ == "__main__":
    des = DES("68/test.bin", "68/out.bin")
    des.generate_subkeys("E0FAE0FEB1F4F8FE")