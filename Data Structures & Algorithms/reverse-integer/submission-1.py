class Solution:
    def reverse(self, x: int) -> int:

        MAX = 2 ** 31 - 1
        MIN = - 2 ** 31

        

        sign = x // abs(x) if x else 1
        new = 0
        x = abs(x)

        while x:
            new *= 10
            new += x % 10
            x = x // 10

        new *= sign
        return 0 if new > MAX or new < MIN else new



