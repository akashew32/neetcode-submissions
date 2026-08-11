class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n = len(s1)
        m = len(s2)
        if n + m != len(s3):
            return False
        if not s3:
            return True
        arr = [[False] * (n + 1) for _ in range(m + 1)]
        arr[-1][-1] = True

        for i in range(m, -1, -1):
            for j in range(n, -1, -1):
                if i < m and arr[i + 1][j] and s2[i] == s3[i + j]:
                    arr[i][j] = True

                if j < n and arr[i][j+1] and s1[j] == s3[i + j]:
                    arr[i][j] = True

        print(arr)
        return arr[0][0]