class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}
        for letter in list(s):
            if letter in freq:
                freq[letter] += 1
            else:
                freq[letter] = 1
        for letter in list(t):
            if letter in freq:
                freq[letter] = freq[letter] - 1
                if freq[letter] == 0:
                    del freq[letter]
            else:
                return False
        if len(freq) == 0:
            return True
        return False