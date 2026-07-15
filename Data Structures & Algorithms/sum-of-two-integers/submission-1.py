class Solution:
    def getSum(self, a: int, b: int) -> int:
        res = 0
        carry = 0
        for i in range(32):
            bit_a = a & 1
            bit_b = b & 1
            res <<= 1
            res |= bit_a ^ bit_b ^ carry
            carry = (bit_a & bit_b) | (bit_b & carry) | (bit_a & carry)

            a >>= 1
            b >>= 1
        res = self.reverseBits(res)
        if res & (1 << 31):
            res -= 1 << 32

        return res


    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            res = res << 1
            res |= (n & 1)
            n >>= 1
        return res
        
