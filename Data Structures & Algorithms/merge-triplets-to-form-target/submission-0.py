class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        curr = [0, 0, 0]
        for trip in triplets:
            flag = True
            for i in range(3):
                if trip[i] > target[i]:
                    flag = False
            
            if flag:
                for i in range(3):
                    curr[i] = max(curr[i], trip[i])
        
        return curr == target