class Solution:
    def findMin(self, nums: List[int]) -> int:
        ## Base case
        if len(nums) == 1:
            return nums[0]
        ## Set bounds for binary search
        l = 0
        r = len(nums) - 1

        ## Check condition for if already sorted (cannot find inconsistency)
        if nums[l] < nums [r]:
            return nums[l]

        while l < r:
            mid = (l + r) // 2
            if mid != len(nums) - 1:
                if nums[mid] > nums [mid + 1]:
                    return nums[mid + 1]
            if nums[mid] > nums[l]:
                l = mid + 1
            elif nums[mid] < nums[l]:
                r = mid
        return nums[-1]