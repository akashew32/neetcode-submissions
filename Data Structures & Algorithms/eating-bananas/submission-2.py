class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        ## Find the largest pile height
        k = max(piles)  
        l = 0
        
        if len(piles) == 1:
            return -(k // -h)
        while l < k - 1:
            mid = (l + k) // 2
            total = 0
            for pile in piles:
                total += -1 * (pile // (-mid))
            if total > h:
                l = mid
            else:
                k = mid
        return k

