class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board  = [["."] * n for i in range(n)]

        def backtrack(r):
            if r == n:
                temp = []
                for row in board:
                    temp.append("".join(row))
                res.append(temp.copy())
                return
            
            for c in range(n):
                if self.compare(r, c, board, n):
                    board[r][c] = "Q"
                    backtrack(r + 1)
                    board[r][c] = "."
            return 

            
            
        
        backtrack(0)
        return res
        

    def compare(self, r: int, c: int, board: List[List[str]], n) -> bool: 
        for i in range(n):
            for j in range(n):
                if board[i][j] == "Q":
                    if i == r or j == c:
                        return False 
                    if abs(i - r) == abs(j - c):
                        return False
        return True





