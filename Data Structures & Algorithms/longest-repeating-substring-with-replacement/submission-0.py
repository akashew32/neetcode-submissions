class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ## Freq map is O(1) size and O(1) operations
        freq = [0] * 26
        r = 0
        l = 0
        longest = 1
        while r < len(s):
            freq[ord(s[r]) - ord("A")] += 1
            while max(freq) + k < r - l + 1:
                freq[ord(s[l]) - ord("A")] -= 1
                l += 1
            longest = max(longest, r - l + 1)
            r += 1

        return longest
            