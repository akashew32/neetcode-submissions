class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        ways = [-1] * (amount + 1)
        ways[0] = 0
        ## 0 indexed array for the smallest way to get each amount
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0 and ways[i - coin] != -1:
                    ways[i] = ways[i-coin] + 1 if ways[i] == -1 else min(ways[i], ways[i-coin] + 1)
        return ways[-1]