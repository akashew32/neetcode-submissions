class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        arr = 0
        arr = [0] * 26

        ## Create a char frequency array for s1
        for char in s1:
            index = ord(char) - ord('a')
            arr[index] += 1
        
        l = 0
        r = len(s1) - 1
        arr2 = [0] * 26
        for i in range(len(s1)):
            index = ord(s2[i]) - ord('a')
            arr2[index] += 1
        if arr2 == arr:
            return True

        while r < len(s2) - 1:
            r += 1
            arr2[ord(s2[r]) - ord('a')] += 1
            arr2[ord(s2[l]) - ord('a')] -= 1
            l += 1
            if arr2 == arr:
                return True
        return False

