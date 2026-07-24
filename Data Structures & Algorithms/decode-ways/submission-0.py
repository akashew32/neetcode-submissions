class Solution:
    def numDecodings(self, s: str) -> int:
        dp1 = 1
        dp = dp2 = 0
        for i in range(len(s) - 1, - 1, -1):
            if s[i] == "0":
                dp = 0
            else:
                dp = dp1
            if i + 1 < len(s) and s[i] != "0" and int(s[i] + s[i+1]) <= 26 and int(s[i] + s[i+1]) > 0:
                dp += dp2
            dp1, dp2 = dp, dp1
            dp = 0
        return dp1