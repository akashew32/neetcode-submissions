class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        map = {}
        for char in text:
            if char not in map:
                map[char] = 0
            map[char] += 1
        curr = 0
        while True:
            for char in "balloon":
                if char not in map:
                    return 0
                if map[char] == 0:
                    return curr
                else:
                    map[char] -= 1
            curr += 1
        return curr