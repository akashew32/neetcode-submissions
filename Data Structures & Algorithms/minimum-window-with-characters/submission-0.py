class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freqt = {}
        freq = {}
        extra = {}
        cs = 0
        ct = 0
        for char in t:
            if char not in freqt:
                freq[char] = 0
                extra[char] = 0
                freqt[char] = 0
            freqt[char] += 1
            ct += 1
        l = 0
        window = [-1000, 1000]
        flag = True
        for r in range(len(s)):
            char = s[r]
            if char in freqt:
                if freq[char] == freqt[char]:
                    extra[char] += 1
                else:
                    freq[char] += 1
                    cs += 1
            while ct == cs:
                if window[1] - window[0] >= r - l:
                    flag = False
                    window = [l, r]
                if s[l] in freqt:
                    if extra[s[l]] > 0:
                        extra[s[l]] -= 1
                    else:
                        freq[s[l]] -= 1
                        cs -= 1
                l += 1
            print(freqt)
            print(freq)
        
        return "" if flag else s[window[0]:window[1] + 1]


