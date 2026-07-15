class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        return max(self.helper(nums[0:len(nums) - 1:]), self.helper(nums[1::]))
    
    def helper(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        for num in nums:
            temp = max(rob1 + num, rob2)
            rob1 = rob2
            rob2 = temp
        
        return max(rob2, rob1)