class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m > n:
            n, m = m, n
        row = [0] * n
        row[0] = 1
        for i in range(m):
            for j in range(n):
                row[j] += row[j-1] if j > 0 else 0
        return row[-1]
                
