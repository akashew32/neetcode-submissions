class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        numset = set(nums)
        res = []
        perm = []

        def backtrack():
            if not numset:
                res.append(perm.copy())
                return
            
            for num in list(numset):
                perm.append(num)
                numset.remove(num)
                backtrack()
                numset.add(num)
                perm.pop()
        
        backtrack()
        return res
                