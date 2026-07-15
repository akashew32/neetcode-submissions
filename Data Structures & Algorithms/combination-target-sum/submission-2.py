class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        path = []
        nums.sort()

        def backtrack(index, total):
            if index == len(nums):
                return
            if total > target:
                return
            if total == target:
                result.append(path.copy()) 
            
            for i in range(index, len(nums)):
                if total + nums[i] > target:
                    break

                path.append(nums[i])

                backtrack(i, total + nums[i])

                path.pop()            
        

        backtrack(0,0)
        return result