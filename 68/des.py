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

    IP = [58, 50, 42, 34, 26, 18, 10, 2,
          60, 52, 44, 36, 28, 20, 12, 4,
          62, 54, 46, 38, 30, 22, 14, 6,
          64, 56, 48, 40, 32, 24, 16, 8,
          57, 49, 41, 33, 25, 17, 9, 1,
          59, 51, 43, 35, 27, 19, 11, 3,
          61, 53, 45, 37, 29, 21, 13, 5,
          63, 55, 47, 39, 31, 23, 15, 7]

    IP_INVERSE = [40, 8, 48, 16, 56, 24, 64, 32,
                  39, 7, 47, 15, 55, 23, 63, 31,
                  38, 6, 46, 14, 54, 22, 62, 30,
                  37, 5, 45, 13, 53, 21, 61, 29,
                  36, 4, 44, 12, 52, 20, 60, 28,
                  35, 3, 43, 11, 51, 19, 59, 27,
                  34, 2, 42, 10, 50, 18, 58, 26,
                  33, 1, 41, 9, 49, 17, 57, 25]

    EXTEND = [32, 1, 2, 3, 4, 5,
         4, 5, 6, 7, 8, 9,
         8, 9, 10, 11, 12, 13,
         12, 13, 14, 15, 16, 17,
         16, 17, 18, 19, 20, 21,
         20, 21, 22, 23, 24, 25,
         24, 25, 26, 27, 28, 29,
         28, 29, 30, 31, 32, 1]

    SBOXES = {0:
                  [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
                   [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
                   [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
                   [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],
              1:
                  [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
                   [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
                   [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
                   [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],
              2:
                  [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
                   [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
                   [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
                   [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],
              3:
                  [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
                   [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
                   [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
                   [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],
              4:
                  [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
                   [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
                   [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
                   [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],
              5:
                  [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
                   [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
                   [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
                   [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],
              6:
                  [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
                   [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
                   [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
                   [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],
              7:
                  [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
                   [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
                   [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
                   [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]}

    P = [16, 7, 20, 21,
         29, 12, 28, 17,
         1, 15, 23, 26,
         5, 18, 31, 10,
         2, 8, 24, 14,
         32, 27, 3, 9,
         19, 13, 30, 6,
         22, 11, 4, 25]

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
                    # TODO implementacja paddingu

                    input_64_bit = "".join(binary_source_block[i:i+8])
                    # TODO przekazac klucz z zewnatrz
                    subkeys = self.generate_subkeys("E0FAE0FEB1F4F8FE")

                    output_64_bit = self.des_algorithm(input_64_bit, subkeys)
                    for j in range(8):
                        binary_destination_block.append(output_64_bit[j*8:j*8+8])
                
                byte_output = self.binary_to_hex(binary_destination_block)

                for byte in byte_output:
                    destination_file.write(byte.to_bytes(1, "big"))

    def des_algorithm(self, input_blok, subkeyes):
        input = self.permutate(input_blok, self.IP)
        left_half= input[:32]
        right_half= input[32:]

        for i in range(16):

            feistel = self.feistel_function(right_half, subkeyes[i])
            right = right_half
            right_half = self.xor(feistel, left_half)
            left_half = right

        out_to_perm = left_half + right_half # TODO sprawdzic czy nie odwrotnie trzeba zlaczyć
        return self.permutate(out_to_perm, self.IP_INVERSE)

    def feistel_function(self, input, key):
        extended_input = self.permutate(input, self.EXTEND)
        xor_link = self.xor(extended_input, key)

        s_blocks = []
        for i in range(0, len(xor_link), 6):
            s_blocks.append(xor_link[i:i+6])

        out_to_perm = ""
        for i in range(len(s_blocks)):
            block = s_blocks[i]

            row_no = int(block[0]) + int(block[5])
            col_no = int(block[1]) + int(block[2]) + int(block[3]) + int(block[4])

            s_box = self.SBOXES[i]

            int_out = s_box[row_no][col_no]
            out_to_perm += "{:04b}".format(int_out)

        return self.permutate(out_to_perm, self.P)


        return ""

    def xor(self, binA, binB):
        out = ""
        for i in range(len(binA)):
            out += str((int(binA[i]) + int(binB[i])) % 2)
        return out

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
