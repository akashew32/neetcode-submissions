class Solution:
    def findMin(self, nums: List[int]) -> int:
        ## Base case
        if len(nums) == 1:
            return nums[0]
        ## Set bounds for binary search
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = (r + l) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else: 
                r = mid
        
        return nums[l]