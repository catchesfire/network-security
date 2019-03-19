
class LFSR:

    def generate_blocks(self, polynomial, seed):
        c = polynomial
        degree = len(c)
        print(c, degree)

        out = [seed]

        for i in range(2 ** degree - 2):
            tmp_sum = 0
            for j in range(degree):
                if c[j] == "1":
                    tmp_sum += int(out[-1][j])
            block = str(tmp_sum % 2)
            for j in range(degree - 1):
                block += out[-1][j]

            out.append(block)

        return out
