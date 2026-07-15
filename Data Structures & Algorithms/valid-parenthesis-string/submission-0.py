class Solution:
    def checkValidString(self, s: str) -> bool:
        maxOpen = 0
        minOpen = 0
        for char in s:
            if char == "(":
                maxOpen += 1
                minOpen += 1
            elif char == ")":
                maxOpen -= 1
                minOpen -= 1
            else:
                maxOpen += 1
                minOpen -= 1
            if maxOpen < 0:
                return False
            if minOpen < 0:
                minOpen = 0
        
        return minOpen == 0
