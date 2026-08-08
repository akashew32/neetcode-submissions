class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        ways = [0] * (1 + amount)
        ways[0] = 1
        for c in coins:
            for i in range(len(ways)):
                if ways[i] != 0 and i + c <= amount:
                    ways[i + c] += ways[i]
        return ways[-1]