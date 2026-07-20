class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        for i in range(len(s)):
            ## Odd palindromes
            r, l = i, i
            while r < len(s) and l >= 0 and s[r] == s[l]:
                count += 1
                r += 1
                l -= 1

            ## Even palindroms
            l, r = i, i + 1
            while r < len(s) and l >= 0 and s[r] == s[l]:
                count += 1
                r += 1
                l -= 1
        return count