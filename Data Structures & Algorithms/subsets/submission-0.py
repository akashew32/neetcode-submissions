class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []
        ret.append([])

        for num in nums:
            for i in range(len(ret)):
                temp = []
                for j in ret[i]:
                    temp.append(j)
                temp.append(num)
                ret.append(temp)

        return ret

    
        