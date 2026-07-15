class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy = prices[0]
        profit = 0

        for sell in prices:
            profit = max(profit, sell - minBuy)
            minBuy = min(minBuy, sell)
        
        return profit