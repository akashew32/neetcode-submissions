class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        prev = nums[2] + nums[0]
        twoPrev = nums[1]
        threePrev = nums[0]
        for i in range(3, len(nums)):
            temp = nums[i] + max(twoPrev, threePrev)
            threePrev = twoPrev
            twoPrev = prev
            prev = temp
        return max(prev, twoPrev)