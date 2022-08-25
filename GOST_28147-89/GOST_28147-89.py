class Gost():
    def __init__(self, key_):
        self.multiplication = 4
        self.number_of_rounds = 8 * self.multiplication
        self.temp = 0
        self.key = key_ & 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        self.round_keys = self.key_gen()
        # print(len(self.round_keys), self.round_keys)

    def Enc(self, temp_):
        self.temp = temp_ & 0xffffffffffffffff
        self.Rounds(encryption=True)
        return self.temp

    def Dec(self, temp_):
        self.temp = temp_ & 0xffffffffffffffff
        self.Rounds(encryption=False)
        return self.temp

    def Sbox(self, block, round_number):
        S = [[3, 8, 15, 1, 10, 6, 5, 11, 14, 13, 4, 2, 7, 0, 9, 12],
             [15, 12, 2, 7, 9, 0, 5, 10, 1, 11, 14, 8, 6, 13, 3, 4],
             [8, 6, 7, 9, 3, 12, 10, 15, 13, 1, 14, 4, 0, 11, 5, 2],
             [0, 15, 11, 8, 12, 9, 6, 3, 13, 1, 2, 4, 10, 7, 5, 14],
             [1, 15, 8, 3, 12, 0, 11, 6, 2, 5, 4, 10, 9, 14, 7, 13],
             [15, 5, 2, 11, 4, 10, 9, 12, 0, 3, 14, 8, 13, 6, 7, 1],
             [7, 2, 12, 5, 8, 4, 6, 11, 14, 9, 1, 15, 13, 3, 10, 0],
             [1, 13, 15, 0, 14, 8, 2, 11, 7, 4, 12, 10, 9, 3, 5, 6]]

        temp_ = 0
        for i in range(8):
            block_ = block >> (28 - (4 * i)) & 0xf
            if round_number > 7:
                round_number = round_number % 8
            temp_ = (temp_ << 4) ^ S[round_number][block_]

        block = temp_

        return block

    def Rounds(self, encryption):
        for i in range(self.number_of_rounds):
            # print('------------------')
            index = i if encryption is True else self.number_of_rounds - i - 1

            left = (self.temp >> 32) & 0xffffffff
            right = (self.temp >> 0) & 0xffffffff
            # print(index, '- before: ', left, right)

            temp = self.FunctionF(left, index)
            right = temp ^ right

            # print(index, '- after: ', left, right)

            if i != (self.number_of_rounds - 1):
                self.temp = (right << 32) ^ left
            else:
                self.temp = (left << 32) ^ right

    def FunctionF(self, N1_, i):
        N1 = (N1_ + self.round_keys[i]) & 0xffffffff
        # print('\t', N1)
        N1 = self.Sbox(N1, i)
        # print('\t', N1)
        N1 = self.Sdvig(N1, 11)
        # print('\t', N1)

        return N1

    def Sdvig(self, x, y_):
        y = y_ % 32
        x = ((x << y) & 0xffffffff) | (x >> 32-y) & 0xffffffff

        return x

    def key_gen(self):
        temp = []
        for i in range(8):
            temp_key = (self.key >> 224 - 32*i) & 0xffffffff
            temp.append(temp_key)
        # print(temp)

        keys = []
        for i in range(self.multiplication):
            for j in range(8):
                if i != (self.multiplication - 1):
                    temp_key = temp[j]
                    keys.append(temp_key)
                else:
                    temp_key = temp[7-j]
                    keys.append(temp_key)

        return keys

    def Enc_file(self, file_path, file_path_enc):
        f1 = open(file_path, 'rb')
        f2 = open(file_path_enc, 'wb')
        while 1:
            temp = f1.read(8)
            if not temp:
                break
            temp = temp if len(temp) == 8 else (temp + b'        ')[0:8:1]
            temp_number = int.from_bytes(temp, 'big')
            temp_number = self.Enc(temp_number)
            temp = temp_number.to_bytes(8, byteorder='big')
            f2.write(temp)
        f1.close()
        f2.close()

    def Dec_file(self, file_path_enc, file_path_dec):
        f1 = open(file_path_enc, 'rb')
        f2 = open(file_path_dec, 'wb')
        while 1:
            temp = f1.read(8)
            if not temp:
                break
            temp = temp if len(temp) == 8 else (temp + b'        ')[0:8:1]
            temp_number = int.from_bytes(temp, 'big')
            temp_number = self.Dec(temp_number)
            temp = temp_number.to_bytes(8, byteorder='big')
            f2.write(temp)
        f1.close()
        f2.close()

gost = Gost(112314235345634634563456500)
enc = gost.Enc_file('enc.txt', 'dec.txt')
print('------------')
dec = gost.Dec_file('dec.txt', 'new.txt')

# a = gost.Enc(12345)
# print(a)
# print('=============')
# b = gost.Dec(a)
# print(b)
