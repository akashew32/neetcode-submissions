class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        half = total // 2
        arr = [False] * (half + 1)
        arr[0] = True
        idxList = []
        for num in nums:
            for i in range(half):
                if num + i <= half and arr[i]:
                    idxList.append(num + i)
            for ind in idxList:
                arr[ind] = True
            idxList = []
        return arr[-1]
        