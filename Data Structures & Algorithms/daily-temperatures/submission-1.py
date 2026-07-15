class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        out = [0] * len(temperatures)

        for i in range(len(temperatures)):
            temp = temperatures[i]
            if not stack:
                stack.append(i)
            else:
                while stack and temp > temperatures[stack[-1]]:
                    index = stack.pop()
                    out[index] = i - index
                stack.append(i)
        
        return out

            