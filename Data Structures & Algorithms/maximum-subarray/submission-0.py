class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        running = -10000
        total = -1000
        for num in nums:
            running = max(running + num, num)
            total = max(total, running)
        return total



    