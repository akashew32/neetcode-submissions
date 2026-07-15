class Solution:
    def trap(self, heights: List[int]) -> int:
        left = list(accumulate(heights, max))
        right = list(accumulate(reversed(heights), max))
        right = right[::-1]
        print(right)
        total = 0
        for i in range(len(heights)):
            total += min(left[i], right[i]) - heights[i]
        
        return total