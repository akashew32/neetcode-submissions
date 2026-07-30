class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    for i in range(COLS):
                        matrix[r][i] += 0.1
                    break
        
        for c in range(COLS):
            for r in range(ROWS):
                if matrix[r][c] == 0 or matrix[r][c] == 0.1:
                    for i in range(ROWS):
                        matrix[i][c] += 0.1
                    break
        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j] // 1 != matrix[i][j]:
                    matrix[i][j] = 0
        
        