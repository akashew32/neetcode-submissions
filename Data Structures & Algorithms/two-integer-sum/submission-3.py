class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        hashSet = {}
        for i in range(len(nums)):
            hashSet[nums[i]] = i
        for i in range(len(nums)):
            if target-nums[i] in hashSet:
                if hashSet[target-nums[i]] != i:
                    return [i, hashSet[target-nums[i]]]
        '''
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i]+nums[j]==target and i!=j:
                    return[i,j]