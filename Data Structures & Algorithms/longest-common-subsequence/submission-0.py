class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        arr = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if text2[i] == text1[j]:
                    arr[i][j] = 1 + arr[i+1][j+1]
                else:
                    arr[i][j] = max(arr[i+1][j], arr[i][j+1])
        return arr[0][0]
                