class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lowerBound = 0
        upperBound = len(nums) - 1
        while upperBound > lowerBound:
            midpoint = (upperBound + lowerBound) // 2
            if nums[midpoint] == target:
                return midpoint
            elif nums[midpoint] > target:
                upperBound = midpoint - 1
            else:
                lowerBound = midpoint + 1
        if nums[lowerBound] == target:
            return lowerBound
        return -1