class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        numset = set()
        res = []
        for num in nums:
            if num in numset:
                res.append(num)
            else:
                numset.add(num)
        
        for i in range(1, len(nums)+ 1):
            if i not in numset:
                res.append(i)
        return res