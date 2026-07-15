class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word = s.split()
        map = {}
        words = set()
        if len(pattern) != len(word):
            return False
        for i in range(len(pattern)):
            char = pattern[i]
            if char not in map and word[i] in words:
                return False
            elif char in map and map[char] != word[i]:
                return False
            else:
                map[char] = word[i]
                words.add(word[i])

        return True
                
                