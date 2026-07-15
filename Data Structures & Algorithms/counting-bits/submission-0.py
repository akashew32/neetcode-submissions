class Solution:
    def countBits(self, n: int) -> List[int]:
        rep = [0] * (n + 1)
        for i in range(1, n + 1):
            rep[i] = rep[i >> 1] + (i & 1)
        
        return rep