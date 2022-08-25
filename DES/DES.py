
class big_des(object):
    def __init__(self, key_, round_amount_):
        self.temp = 0
        self.key = key_ & 0b1111111111111111111111111111111111111111111111111111111111111111
        self.round_amount = round_amount_
        self.round_key = self.key_gen()

    def Enc(self, temp_):
        self.temp = temp_ & 0b1111111111111111111111111111111111111111111111111111111111111111

        self.PblockBegin()

        i = 0
        while i < self.round_amount:
            self.Round(self.round_key[i])
            i = i + 1
        self.ChangeLeftRight()

        self.PblockEnd()

        return self.temp

    def Dec(self, temp_):
        self.temp = temp_ & 0b1111111111111111111111111111111111111111111111111111111111111111

        self.PblockBegin()

        i = 0
        while i < self.round_amount:
            self.Round(self.round_key[self.round_amount - i - 1])
            i = i + 1
        self.ChangeLeftRight()

        self.PblockEnd()

        return self.temp

    def PblockBegin(self):
        self.temp = ((self.temp & 0b0000000000000000000000000000000000000000000000000000000001000000) << 57) | \
                    ((self.temp & 0b0000000000000000000000000000000000000000000000000100000000000000) << 48) | \
                    ((self.temp & 0b0000000000000000000000000000000000000000010000000000000000000000) << 39) | \
                    ((self.temp & 0b0000000000000000000000000000000001000000000000000000000000000000) << 30) | \
                    ((self.temp & 0b0000000000000000000000000100000000000000000000000000000000000000) << 21) | \
                    ((self.temp & 0b0000000000000000010000000000000000000000000000000000000000000000) << 12) | \
                    ((self.temp & 0b0000000001000000000000000000000000000000000000000000000000000000) << 3) | \
                    ((self.temp & 0b0100000000000000000000000000000000000000000000000000000000000000) >> 6) | \
                    ((self.temp & 0b0000000000000000000000000000000000000000000000000000000000010000) << 51) | \
                    ((self.temp & 0b0000000000000000000000000000000000000000000000000001000000000000) << 42) | \
                    ((self.temp & 0b0000000000000000000000000000000000000000000100000000000000000000) << 33) | \
                    ((self.temp & 0b0000000000000000000000000000000000010000000000000000000000000000) << 24) | \
                    ((self.temp & 0b0000000000000000000000000001000000000000000000000000000000000000) << 15) | \
                    ((self.temp & 0b0000000000000000000100000000000000000000000000000000000000000000) << 6) | \
                    ((self.temp & 0b0000000000010000000000000000000000000000000000000000000000000000) >> 3) | \
                    ((self.temp & 0b0001000000000000000000000000000000000000000000000000000000000000) >> 12) | \
                    ((self.temp & 0b0000000000000000000000000000000000000000000000000000000000000100) << 45) | \
                    ((self.temp & 0b0000000000000000000000000000000000000000000000000000010000000000) << 36) | \
                    ((self.temp & 0b0000000000000000000000000000000000000000000001000000000000000000) << 27) | \
                    ((self.temp & 0b0000000000000000000000000000000000000100000000000000000000000000) << 18) | \
                    ((self.temp & 0b0000000000000000000000000000010000000000000000000000000000000000) << 9) | \
                    ((self.temp & 0b0000000000000000000001000000000000000000000000000000000000000000) << 0) | \
                    ((self.temp & 0b0000000000000100000000000000000000000000000000000000000000000000) >> 9) | \
                    ((self.temp & 0b0000010000000000000000000000000000000000000000000000000000000000) >> 18) | \
                    ((self.temp & 0b0000000000000000000000000000000000000000000000000000000000000001) << 39) | \
                    ((self.temp & 0b0000000000000000000000000000000000000000000000000000000100000000) << 30) | \
                    ((self.temp & 0b0000000000000000000000000000000000000000000000010000000000000000) << 21) | \
                    ((self.temp & 0b0000000000000000000000000000000000000001000000000000000000000000) << 12) | \
                    ((self.temp & 0b0000000000000000000000000000000100000000000000000000000000000000) << 3) | \
                    ((self.temp & 0b0000000000000000000000010000000000000000000000000000000000000000) >> 6) | \
                    ((self.temp & 0b0000000000000001000000000000000000000000000000000000000000000000) >> 15) | \
                    ((self.temp & 0b0000000100000000000000000000000000000000000000000000000000000000) >> 24) | \
                    ((self.temp & 0b0000000000000000000000000000000000000000000000000000000010000000) << 24) | \
                    ((self.temp & 0b0000000000000000000000000000000000000000000000001000000000000000) << 15) | \
                    ((self.temp & 0b0000000000000000000000000000000000000000100000000000000000000000) << 6) | \
                    ((self.temp & 0b0000000000000000000000000000000010000000000000000000000000000000) >> 3) | \
                    ((self.temp & 0b0000000000000000000000001000000000000000000000000000000000000000) >> 12) | \
                    ((self.temp & 0b0000000000000000100000000000000000000000000000000000000000000000) >> 21) | \
                    ((self.temp & 0b0000000010000000000000000000000000000000000000000000000000000000) >> 30) | \
                    ((self.temp & 0b1000000000000000000000000000000000000000000000000000000000000000) >> 39) | \
                    ((self.temp & 0b0000000000000000000000000000000000000000000000000000000000100000) << 18) | \
                    ((self.temp & 0b0000000000000000000000000000000000000000000000000010000000000000) << 9) | \
                    ((self.temp & 0b0000000000000000000000000000000000000000001000000000000000000000) << 0) | \
                    ((self.temp & 0b0000000000000000000000000000000000100000000000000000000000000000) >> 9) | \
                    ((self.temp & 0b0000000000000000000000000010000000000000000000000000000000000000) >> 18) | \
                    ((self.temp & 0b0000000000000000001000000000000000000000000000000000000000000000) >> 27) | \
                    ((self.temp & 0b0000000000100000000000000000000000000000000000000000000000000000) >> 36) | \
                    ((self.temp & 0b0010000000000000000000000000000000000000000000000000000000000000) >> 45) | \
                    ((self.temp & 0b0000000000000000000000000000000000000000000000000000000000001000) << 12) | \
                    ((self.temp & 0b0000000000000000000000000000000000000000000000000000100000000000) << 3) | \
                    ((self.temp & 0b0000000000000000000000000000000000000000000010000000000000000000) >> 6) | \
                    ((self.temp & 0b0000000000000000000000000000000000001000000000000000000000000000) >> 15) | \
                    ((self.temp & 0b0000000000000000000000000000100000000000000000000000000000000000) >> 24) | \
                    ((self.temp & 0b0000000000000000000010000000000000000000000000000000000000000000) >> 33) | \
                    ((self.temp & 0b0000000000001000000000000000000000000000000000000000000000000000) >> 42) | \
                    ((self.temp & 0b0000100000000000000000000000000000000000000000000000000000000000) >> 51) | \
                    ((self.temp & 0b0000000000000000000000000000000000000000000000000000000000000010) << 6) | \
                    ((self.temp & 0b0000000000000000000000000000000000000000000000000000001000000000) >> 3) | \
                    ((self.temp & 0b0000000000000000000000000000000000000000000000100000000000000000) >> 12) | \
                    ((self.temp & 0b0000000000000000000000000000000000000010000000000000000000000000) >> 21) | \
                    ((self.temp & 0b0000000000000000000000000000001000000000000000000000000000000000) >> 30) | \
                    ((self.temp & 0b0000000000000000000000100000000000000000000000000000000000000000) >> 39) | \
                    ((self.temp & 0b0000000000000010000000000000000000000000000000000000000000000000) >> 48) | \
                    ((self.temp & 0b0000001000000000000000000000000000000000000000000000000000000000) >> 57)

    def PblockEnd(self):
        self.temp = ((self.temp & 0b0000000000000000000000000000000000000001000000000000000000000000) << 39) | \
                    ((self.temp & 0b0000000100000000000000000000000000000000000000000000000000000000) << 6) | \
                    ((self.temp & 0b0000000000000000000000000000000000000000000000010000000000000000) << 45) | \
                    ((self.temp & 0b0000000000000001000000000000000000000000000000000000000000000000) << 12) | \
                    ((self.temp & 0b0000000000000000000000000000000000000000000000000000000100000000) << 51) | \
                    ((self.temp & 0b0000000000000000000000010000000000000000000000000000000000000000) << 18) | \
                    ((self.temp & 0b0000000000000000000000000000000000000000000000000000000000000001) << 57) | \
                    ((self.temp & 0b0000000000000000000000000000000100000000000000000000000000000000) << 24) | \
                    ((self.temp & 0b0000000000000000000000000000000000000010000000000000000000000000) << 30) | \
                    ((self.temp & 0b0000001000000000000000000000000000000000000000000000000000000000) >> 3) | \
                    ((self.temp & 0b0000000000000000000000000000000000000000000000100000000000000000) << 36) | \
                    ((self.temp & 0b0000000000000010000000000000000000000000000000000000000000000000) << 3) | \
                    ((self.temp & 0b0000000000000000000000000000000000000000000000000000001000000000) << 42) | \
                    ((self.temp & 0b0000000000000000000000100000000000000000000000000000000000000000) << 9) | \
                    ((self.temp & 0b0000000000000000000000000000000000000000000000000000000000000010) << 48) | \
                    ((self.temp & 0b0000000000000000000000000000001000000000000000000000000000000000) << 15) | \
                    ((self.temp & 0b0000000000000000000000000000000000000100000000000000000000000000) << 21) | \
                    ((self.temp & 0b0000010000000000000000000000000000000000000000000000000000000000) >> 12) | \
                    ((self.temp & 0b0000000000000000000000000000000000000000000001000000000000000000) << 27) | \
                    ((self.temp & 0b0000000000000100000000000000000000000000000000000000000000000000) >> 6) | \
                    ((self.temp & 0b0000000000000000000000000000000000000000000000000000010000000000) << 33) | \
                    ((self.temp & 0b0000000000000000000001000000000000000000000000000000000000000000) << 0) | \
                    ((self.temp & 0b0000000000000000000000000000000000000000000000000000000000000100) << 39) | \
                    ((self.temp & 0b0000000000000000000000000000010000000000000000000000000000000000) << 6) | \
                    ((self.temp & 0b0000000000000000000000000000000000001000000000000000000000000000) << 12) | \
                    ((self.temp & 0b0000100000000000000000000000000000000000000000000000000000000000) >> 21) | \
                    ((self.temp & 0b0000000000000000000000000000000000000000000010000000000000000000) << 18) | \
                    ((self.temp & 0b0000000000001000000000000000000000000000000000000000000000000000) >> 15) | \
                    ((self.temp & 0b0000000000000000000000000000000000000000000000000000100000000000) << 24) | \
                    ((self.temp & 0b0000000000000000000010000000000000000000000000000000000000000000) >> 9) | \
                    ((self.temp & 0b0000000000000000000000000000000000000000000000000000000000001000) << 30) | \
                    ((self.temp & 0b0000000000000000000000000000100000000000000000000000000000000000) >> 3) | \
                    ((self.temp & 0b0000000000000000000000000000000000010000000000000000000000000000) << 3) | \
                    ((self.temp & 0b0001000000000000000000000000000000000000000000000000000000000000) >> 30) | \
                    ((self.temp & 0b0000000000000000000000000000000000000000000100000000000000000000) << 9) | \
                    ((self.temp & 0b0000000000010000000000000000000000000000000000000000000000000000) >> 24) | \
                    ((self.temp & 0b0000000000000000000000000000000000000000000000000001000000000000) << 15) | \
                    ((self.temp & 0b0000000000000000000100000000000000000000000000000000000000000000) >> 18) | \
                    ((self.temp & 0b0000000000000000000000000000000000000000000000000000000000010000) << 21) | \
                    ((self.temp & 0b0000000000000000000000000001000000000000000000000000000000000000) >> 12) | \
                    ((self.temp & 0b0000000000000000000000000000000000100000000000000000000000000000) >> 6) | \
                    ((self.temp & 0b0010000000000000000000000000000000000000000000000000000000000000) >> 39) | \
                    ((self.temp & 0b0000000000000000000000000000000000000000001000000000000000000000) << 0) | \
                    ((self.temp & 0b0000000000100000000000000000000000000000000000000000000000000000) >> 33) | \
                    ((self.temp & 0b0000000000000000000000000000000000000000000000000010000000000000) << 6) | \
                    ((self.temp & 0b0000000000000000001000000000000000000000000000000000000000000000) >> 27) | \
                    ((self.temp & 0b0000000000000000000000000000000000000000000000000000000000100000) << 12) | \
                    ((self.temp & 0b0000000000000000000000000010000000000000000000000000000000000000) >> 21) | \
                    ((self.temp & 0b0000000000000000000000000000000001000000000000000000000000000000) >> 15) | \
                    ((self.temp & 0b0100000000000000000000000000000000000000000000000000000000000000) >> 48) | \
                    ((self.temp & 0b0000000000000000000000000000000000000000010000000000000000000000) >> 9) | \
                    ((self.temp & 0b0000000001000000000000000000000000000000000000000000000000000000) >> 42) | \
                    ((self.temp & 0b0000000000000000000000000000000000000000000000000100000000000000) >> 3) | \
                    ((self.temp & 0b0000000000000000010000000000000000000000000000000000000000000000) >> 36) | \
                    ((self.temp & 0b0000000000000000000000000000000000000000000000000000000001000000) << 3) | \
                    ((self.temp & 0b0000000000000000000000000100000000000000000000000000000000000000) >> 30) | \
                    ((self.temp & 0b0000000000000000000000000000000010000000000000000000000000000000) >> 24) | \
                    ((self.temp & 0b1000000000000000000000000000000000000000000000000000000000000000) >> 57) | \
                    ((self.temp & 0b0000000000000000000000000000000000000000100000000000000000000000) >> 18) | \
                    ((self.temp & 0b0000000010000000000000000000000000000000000000000000000000000000) >> 51) | \
                    ((self.temp & 0b0000000000000000000000000000000000000000000000001000000000000000) >> 12) | \
                    ((self.temp & 0b0000000000000000100000000000000000000000000000000000000000000000) >> 45) | \
                    ((self.temp & 0b0000000000000000000000000000000000000000000000000000000010000000) >> 6) | \
                    ((self.temp & 0b0000000000000000000000001000000000000000000000000000000000000000) >> 39)

    def Round(self, round_key):
        left = ((self.temp & 0b1111111111111111111111111111111100000000000000000000000000000000) >> 32)
        right = ((self.temp & 0b0000000000000000000000000000000011111111111111111111111111111111) >> 0)
        tempF = self.FunctionF(right, round_key)
        left = left ^ tempF
        self.temp = (right << 32) | left

    def FunctionF(self, right, round_key):
        # P-block expansion
        a = right
        a = bin(a) + '0000000000000000'
        a = int(a, 2)
        right = a

        right = ((right & 0b000000000000000000000000000000010000000000000000) << 31) | \
                ((right & 0b111110000000000000000000000000000000000000000000) >> 1) | \
                ((right & 0b000110000000000000000000000000000000000000000000) >> 3) | \
                ((right & 0b000001111000000000000000000000000000000000000000) >> 3) | \
                ((right & 0b000000011000000000000000000000000000000000000000) >> 5) | \
                ((right & 0b000000000111100000000000000000000000000000000000) >> 5) | \
                ((right & 0b000000000001100000000000000000000000000000000000) >> 7) | \
                ((right & 0b000000000000011110000000000000000000000000000000) >> 7) | \
                ((right & 0b000000000000000110000000000000000000000000000000) >> 9) | \
                ((right & 0b000000000000000001111000000000000000000000000000) >> 9) | \
                ((right & 0b000000000000000000011000000000000000000000000000) >> 11) | \
                ((right & 0b000000000000000000000111100000000000000000000000) >> 11) | \
                ((right & 0b000000000000000000000001100000000000000000000000) >> 13) | \
                ((right & 0b000000000000000000000000011110000000000000000000) >> 13) | \
                ((right & 0b000000000000000000000000000110000000000000000000) >> 15) | \
                ((right & 0b000000000000000000000000000001110000000000000000) >> 15) | \
                ((right & 0b100000000000000000000000000000000000000000000000) >> 47)

        # XOR
        result = right ^ round_key

        Sbox = [
            #Sbox1
            14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7,
            0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8,
            4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0,
            15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13,

            #Sbox2
            15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10,
            3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5,
            0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15,
            13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9,

            #Sbox3
            10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8,
            13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1,
            13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7,
            1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12,

            #Sbox4
            7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15,
            13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9,
            10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4,
            3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14,

            #Sbox5
            2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9,
            14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6,
            4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14,
            11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3,

            #Sbox6
            12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11,
            10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8,
            9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6,
            4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13,

            #Sbox7
            4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1,
            13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6,
            1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2,
            6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12,

            #Sbox8
            13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7,
            1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2,
            7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8,
            2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11

        ]

        res = 0
        i = 0
        mas = [
            0b111111000000000000000000000000000000000000000000,
            0b000000111111000000000000000000000000000000000000,
            0b000000000000111111000000000000000000000000000000,
            0b000000000000000000111111000000000000000000000000,
            0b000000000000000000000000111111000000000000000000,
            0b000000000000000000000000000000111111000000000000,
            0b000000000000000000000000000000000000111111000000,
            0b000000000000000000000000000000000000000000111111
        ]
        while i < 8:
            col1 = ((result & mas[i]) >> (42-i*6))
            index = ((col1 & 0b100000) << 0) | \
                    ((col1 & 0b000001) << 4) | \
                    ((col1 & 0b011110) >> 1)
            res = res ^ ((Sbox[index+64*i] & 0b111111) << (42-i*6))
            i=i+1

        result = res

        # P-box
        result = ((result & 0b00000000000000010000000000000000) << 15) | \
                 ((result & 0b00000010000000000000000000000000) << 5) | \
                 ((result & 0b00000000000000000001000000000000) << 17) | \
                 ((result & 0b00000000000000000000100000000000) << 17) | \
                 ((result & 0b00000000000000000000000000001000) << 24) | \
                 ((result & 0b00000000000100000000000000000000) << 6) | \
                 ((result & 0b00000000000000000000000000010000) << 21) | \
                 ((result & 0b00000000000000001000000000000000) << 9) | \
                 ((result & 0b10000000000000000000000000000000) >> 8) | \
                 ((result & 0b00000000000000100000000000000000) << 5) | \
                 ((result & 0b00000000000000000000001000000000) << 12) | \
                 ((result & 0b00000000000000000000000001000000) << 14) | \
                 ((result & 0b00001000000000000000000000000000) >> 8) | \
                 ((result & 0b00000000000000000100000000000000) << 4) | \
                 ((result & 0b00000000000000000000000000000010) << 16) | \
                 ((result & 0b00000000010000000000000000000000) >> 6) | \
                 ((result & 0b01000000000000000000000000000000) >> 15) | \
                 ((result & 0b00000001000000000000000000000000) >> 10) | \
                 ((result & 0b00000000000000000000000100000000) << 5) | \
                 ((result & 0b00000000000001000000000000000000) >> 6) | \
                 ((result & 0b00000000000000000000000000000001) << 11) | \
                 ((result & 0b00000000000000000000000000100000) << 5) | \
                 ((result & 0b00100000000000000000000000000000) >> 20) | \
                 ((result & 0b00000000100000000000000000000000) >> 15) | \
                 ((result & 0b00000000000000000010000000000000) >> 6) | \
                 ((result & 0b00000000000010000000000000000000) >> 13) | \
                 ((result & 0b00000000000000000000000000000100) << 3) | \
                 ((result & 0b00000100000000000000000000000000) >> 22) | \
                 ((result & 0b00000000000000000000010000000000) >> 7) | \
                 ((result & 0b00000000001000000000000000000000) >> 19) | \
                 ((result & 0b00010000000000000000000000000000) >> 27) | \
                 ((result & 0b00000000000000000000000010000000) >> 7)

        return result

    def ChangeLeftRight(self):
        self.temp = ((self.temp & 0b1111111111111111111111111111111100000000000000000000000000000000) >> 32) | \
                    ((self.temp & 0b0000000000000000000000000000000011111111111111111111111111111111) << 32)

    def key_gen(self):
        key_temp = (self.key & 0xFFFFFFFFFFFFFFFF)
        C0D0 = (((key_temp & 0x39) >> 56) << 55) | \
               (((key_temp & 0x31) >> 48) << 54) | \
               (((key_temp & 0x29) >> 40) << 53) | \
               (((key_temp & 0x21) >> 32) << 52) | \
               (((key_temp & 0x19) >> 24) << 51) | \
               (((key_temp & 0x11) >> 16) << 50) | \
               (((key_temp & 0x9) >> 8) << 49) | \
               (((key_temp & 0x1) >> 0) << 48) | \
               (((key_temp & 0x3a) >> 57) << 47) | \
               (((key_temp & 0x32) >> 49) << 46) | \
               (((key_temp & 0x2a) >> 41) << 45) | \
               (((key_temp & 0x22) >> 33) << 44) | \
               (((key_temp & 0x1a) >> 25) << 43) | \
               (((key_temp & 0x12) >> 17) << 42) | \
               (((key_temp & 0xa) >> 9) << 41) | \
               (((key_temp & 0x2) >> 1) << 40) | \
               (((key_temp & 0x3b) >> 58) << 39) | \
               (((key_temp & 0x33) >> 50) << 38) | \
               (((key_temp & 0x2b) >> 42) << 37) | \
               (((key_temp & 0x23) >> 34) << 36) | \
               (((key_temp & 0x1b) >> 26) << 35) | \
               (((key_temp & 0x13) >> 18) << 34) | \
               (((key_temp & 0xb) >> 10) << 33) | \
               (((key_temp & 0x2) >> 2) << 32) | \
               (((key_temp & 0x3c) >> 59) << 31) | \
               (((key_temp & 0x34) >> 51) << 30) | \
               (((key_temp & 0x2c) >> 43) << 29) | \
               (((key_temp & 0x24) >> 35) << 28) | \
               (((key_temp & 0x3f) >> 62) << 27) | \
               (((key_temp & 0x37) >> 54) << 26) | \
               (((key_temp & 0x2f) >> 46) << 25) | \
               (((key_temp & 0x27) >> 38) << 24) | \
               (((key_temp & 0x1f) >> 30) << 23) | \
               (((key_temp & 0x17) >> 22) << 22) | \
               (((key_temp & 0xf) >> 14) << 21) | \
               (((key_temp & 0x7) >> 6) << 20) | \
               (((key_temp & 0x3e) >> 61) << 19) | \
               (((key_temp & 0x36) >> 53) << 18) | \
               (((key_temp & 0x2e) >> 45) << 17) | \
               (((key_temp & 0x26) >> 37) << 16) | \
               (((key_temp & 0x1e) >> 29) << 15) | \
               (((key_temp & 0x16) >> 21) << 14) | \
               (((key_temp & 0xe) >> 13) << 13) | \
               (((key_temp & 0x5) >> 5) << 12) | \
               (((key_temp & 0x3d) >> 60) << 11) | \
               (((key_temp & 0x35) >> 52) << 10) | \
               (((key_temp & 0x2d) >> 44) << 9) | \
               (((key_temp & 0x25) >> 36) << 8) | \
               (((key_temp & 0x1d) >> 28) << 7) | \
               (((key_temp & 0x15) >> 20) << 6) | \
               (((key_temp & 0xd) >> 12) << 5) | \
               (((key_temp & 0x5) >> 4) << 4) | \
               (((key_temp & 0x1c) >> 27) << 3) | \
               (((key_temp & 0x14) >> 19) << 2) | \
               (((key_temp & 0xc) >> 11) << 1) | \
               (((key_temp & 0x4) >> 3) << 0)

        C0 = ((C0D0 & 0b11111111111111111111111111110000000000000000000000000000) >> 28)
        D0 = ((C0D0 & 0b00000000000000000000000000001111111111111111111111111111) >> 0)

        i = 0
        key_list = []
        while i < self.round_amount:
            if i in [0, 1, 8, 15]:
                C0 = ((C0 << 1) & 0xFFFFFFF) ^ ((C0 >> 27) & 0x1)
                D0 = ((D0 << 1) & 0xFFFFFFF) ^ ((D0 >> 27) & 0x1)
            else:
                C0 = ((C0 << 2) & 0xFFFFFFF) ^ ((C0 >> 27) & 0x3)
                D0 = ((D0 << 2) & 0xFFFFFFF) ^ ((D0 >> 27) & 0x3)

            #print(C0, D0)
            C0D0_temp = ((C0 << 28) & 0xFFFFFFFFFFFFFF) ^ (D0 & 0xFFFFFFF)

            round_key = (((C0D0_temp & 0xe) >> 13) << 47) | \
                        (((C0D0_temp & 0x11) >> 16) << 46) | \
                        (((C0D0_temp & 0xb) >> 10) << 45) | \
                        (((C0D0_temp & 0x18) >> 23) << 44) | \
                        (((C0D0_temp & 0x1) >> 0) << 43) | \
                        (((C0D0_temp & 0x5) >> 4) << 42) | \
                        (((C0D0_temp & 0x3) >> 2) << 41) | \
                        (((C0D0_temp & 0x1b) >> 27) << 40) | \
                        (((C0D0_temp & 0xf) >> 14) << 39) | \
                        (((C0D0_temp & 0x5) >> 5) << 38) | \
                        (((C0D0_temp & 0x15) >> 20) << 37) | \
                        (((C0D0_temp & 0xa) >> 9) << 36) | \
                        (((C0D0_temp & 0x17) >> 22) << 35) | \
                        (((C0D0_temp & 0x13) >> 18) << 34) | \
                        (((C0D0_temp & 0xc) >> 11) << 33) | \
                        (((C0D0_temp & 0x4) >> 3) << 32) | \
                        (((C0D0_temp & 0x1a) >> 25) << 31) | \
                        (((C0D0_temp & 0x8) >> 7) << 30) | \
                        (((C0D0_temp & 0x10) >> 15) << 29) | \
                        (((C0D0_temp & 0x7) >> 6) << 28) | \
                        (((C0D0_temp & 0x1b) >> 26) << 27) | \
                        (((C0D0_temp & 0x14) >> 19) << 26) | \
                        (((C0D0_temp & 0xd) >> 12) << 25) | \
                        (((C0D0_temp & 0x2) >> 1) << 24) | \
                        (((C0D0_temp & 0x29) >> 40) << 23) | \
                        (((C0D0_temp & 0x33) >> 51) << 22) | \
                        (((C0D0_temp & 0x1f) >> 30) << 21) | \
                        (((C0D0_temp & 0x25) >> 36) << 20) | \
                        (((C0D0_temp & 0x2f) >> 46) << 19) | \
                        (((C0D0_temp & 0x37) >> 54) << 18) | \
                        (((C0D0_temp & 0x1e) >> 29) << 17) | \
                        (((C0D0_temp & 0x28) >> 39) << 16) | \
                        (((C0D0_temp & 0x33) >> 50) << 15) | \
                        (((C0D0_temp & 0x2d) >> 44) << 14) | \
                        (((C0D0_temp & 0x21) >> 32) << 13) | \
                        (((C0D0_temp & 0x30) >> 47) << 12) | \
                        (((C0D0_temp & 0x2c) >> 43) << 11) | \
                        (((C0D0_temp & 0x31) >> 48) << 10) | \
                        (((C0D0_temp & 0x27) >> 38) << 9) | \
                        (((C0D0_temp & 0x38) >> 55) << 8) | \
                        (((C0D0_temp & 0x22) >> 33) << 7) | \
                        (((C0D0_temp & 0x35) >> 52) << 6) | \
                        (((C0D0_temp & 0x2e) >> 45) << 5) | \
                        (((C0D0_temp & 0x2a) >> 41) << 4) | \
                        (((C0D0_temp & 0x32) >> 49) << 3) | \
                        (((C0D0_temp & 0x24) >> 35) << 2) | \
                        (((C0D0_temp & 0x1d) >> 28) << 1) | \
                        (((C0D0_temp & 0x20) >> 31) << 0)

            key_list.append(round_key)
            i = i + 1

        return key_list

    #Enc/Dec files
    def Enc_file(self, file_path, file_path_enc, IV=5, k=8, flag = 'ECB'):

        def ECB(file_path, file_path_enc):
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

        def CBC(file_path, file_path_enc, IV):
            f1 = open(file_path, 'rb')
            f2 = open(file_path_enc, 'wb')

            C = IV
            while 1:
                temp = f1.read(8)
                if not temp:
                    break
                temp = temp if len(temp) == 8 else (temp + b'        ')[0:8:1]
                temp_number = int.from_bytes(temp, 'big')
                C = C ^ temp_number
                C = self.Enc(C)
                f2.write(C.to_bytes(8, byteorder='big'))
            f1.close()
            f2.close()

        def CFB(file_path, file_path_enc, IV, k):
            f1 = open(file_path, 'rb')
            f2 = open(file_path_enc, 'wb')

            C = self.Enc(IV)
            while 1:
                temp = f1.read(k)
                if not temp:
                    break
                temp = temp if len(temp) == 8 else (temp + b'        ')[0:8:1]
                temp_number = int.from_bytes(temp, 'big')
                temp_number = C ^ temp_number
                C = self.Enc(C)
                f2.write(temp_number.to_bytes(k, byteorder='big'))
            f1.close()
            f2.close()

        if flag == 'ECB':
            ECB(file_path, file_path_enc)
        elif flag == 'CBC':
            CBC(file_path, file_path_enc, IV)
        elif flag == 'CFB':
            CFB(file_path, file_path_enc, IV, k)

    def Dec_file(self, file_path_enc, file_path_dec, IV=5, k=8, flag = 'ECB'):

        def ECB(file_path_enc, file_path_dec):
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

        def CBC(file_path_enc, file_path_dec, IV):
            f1 = open(file_path_enc, 'rb')
            f2 = open(file_path_dec, 'wb')

            C1 = IV
            C2 = 0
            while 1:
                temp = f1.read(8)
                if not temp:
                    break
                temp = temp if len(temp) == 8 else (temp + b'        ')[0:8:1]
                temp_number = int.from_bytes(temp, 'big')
                C2 = temp_number
                temp_number = self.Dec(temp_number)
                temp_number = temp_number ^ C1
                C1 = C2
                f2.write(temp_number.to_bytes(8, byteorder='big'))
            f1.close()
            f2.close()

        def CFB(file_path_enc, file_path_dec, IV, k):
            f1 = open(file_path_enc, 'rb')
            f2 = open(file_path_dec, 'wb')

            C = self.Enc(IV)
            while 1:
                temp = f1.read(k)
                if not temp:
                    break
                temp = temp if len(temp) == 8 else (temp + b'        ')[0:8:1]
                temp_number = int.from_bytes(temp, 'big')
                temp_number = C ^ temp_number
                C = self.Enc(C)
                f2.write(temp_number.to_bytes(k, byteorder='big'))
            f1.close()
            f2.close()

        if flag == 'ECB':
            ECB(file_path_enc, file_path_dec)
        elif flag == 'CBC':
            CBC(file_path_enc, file_path_dec, IV)
        elif flag == 'CFB':
            CFB(file_path_enc, file_path_dec, IV, k)


a = 0x123456ABCD132536
print(f'a = {a}')
key = 0xAABB09182736CCDD
round_amount = 16
DES = big_des(key_=key, round_amount_=round_amount)

from PIL import Image


r = DES.Enc_file('/photo.jpg', 'photo1.jpg')
# f = DES.Dec_file('dec.txt', 'new.txt')
