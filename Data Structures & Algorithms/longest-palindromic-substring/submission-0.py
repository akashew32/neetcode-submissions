class Solution:
    def longestPalindrome(self, s: str) -> str:
        idx = 0
        maxLen = 1
        for i in range(len(s)):
            ## Check odd Length Palindrome
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > maxLen:
                    maxLen = r - l + 1
                    idx = l
                l -= 1
                r += 1
                
            ## Check even Length Palindrome
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > maxLen:
                    maxLen = r - l + 1
                    idx = l
                l -= 1
                r += 1
        return s[idx:idx+maxLen]







