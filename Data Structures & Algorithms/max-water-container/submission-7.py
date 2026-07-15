class Solution:
    def maxArea(self, heights: List[int]) -> int:
        p1 = 0
        p2 = len(heights) - 1
        area = min(heights[p1], heights[p2]) * (p2 - p1)
        while p1 < p2:
            if heights[p1] < heights[p2]:
                p1 += 1
                cand = min(heights[p1], heights[p2]) * (p2 - p1)
                area = max(area, cand)
            else: 
                p2 -= 1
                cand = min(heights[p1], heights[p2]) * (p2 - p1)
                area = max(area,cand)  
        return area