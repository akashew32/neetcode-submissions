class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        arr = [False] * (len(s) + 1)
        arr[0] = True

        for i in range(len(s)):
            for word in wordDict:
                m = len(word)
                if i - m + 1 >= 0 and not arr[i + 1]:
                    arr[i + 1] = arr[i - m + 1] and s[i-m+1:i+1] == word
        return arr[-1]