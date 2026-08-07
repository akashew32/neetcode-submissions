class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if abs(target) > total:
            return 0
        arr = [0] * (2 * total + 1)
        arr[total] = 1
        res = 0
        for j in range(len(nums)):
            num = nums[j]
            newArr = [0] * (2 * total + 1)
            for i in range(len(arr)):
                if arr[i]:
                    newArr[i - num] += arr[i]
                    newArr[i + num] += arr[i]
            arr = newArr
        
        return arr[total + target]