class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxVal = nums[0]
        curr = curr = nums[0]
        currmin = nums[0]
        sign = 1
        for i in range(1, len(nums)):
            num = nums[i]
            temp = curr
            curr = max(num, num * curr, num * currmin)
            currmin = min(num, num * currmin, num * temp)
            maxVal = max(maxVal, curr, currmin)
        return maxVal