class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashSet = set()
        longestSubstring = 1
        if not s:
            return 0
        l = 0
        hashSet.add(s[l])
        for r in range(1, len(s)):
            if s[r] in hashSet:
                while s[r] in hashSet:
                    hashSet.remove(s[l])
                    l += 1

            hashSet.add(s[r])

            longestSubstring = max(longestSubstring, len(hashSet))
        
        return longestSubstring