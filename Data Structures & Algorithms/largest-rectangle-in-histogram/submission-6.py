class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        area = 0
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                temp = stack.pop()
                if stack:
                    left = stack[-1] + 1
                else:
                    left = 0
                area = max(area, heights[temp] * (i - left))
            
            stack.append(i)
        print(stack)
        print(area)
        for i in range(len(stack)):
            if i == 0:
                area = max(area, heights[stack[i]] * len(heights))
                continue
            temp = heights[stack[i]] * (stack[-1] - stack[i - 1])
            area = max(area, temp)
        return area
