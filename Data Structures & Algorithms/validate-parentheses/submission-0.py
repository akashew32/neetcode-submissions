class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in ['(', '[', '{']:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                prev = stack.pop()
                if prev + char != '()' and prev + char != '[]' and prev + char != '{}':
                    return False
        if len(stack) == 0:
            return True
        return False