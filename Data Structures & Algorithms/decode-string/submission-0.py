class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr = "" 
        nums = []
        for char in s:
            if char.isdigit():
                nums.append(char)
            elif char == "[":
                mul = int("".join(nums))
                stack.append((curr, mul))
                curr = ""
                nums = []
            elif char == "]":
                tup = stack.pop()
                curr = tup[0] + tup[1] * curr
            else: 
                curr += char
        return curr