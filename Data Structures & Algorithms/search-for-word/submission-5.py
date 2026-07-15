class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        res = False
        rows = len(board)
        cols = len(board[0])
        path = []

        def backtrack(r, c, i):
            nonlocal res
            nonlocal rows
            nonlocal cols
            if i >= len(word):
                res = True
                return
            
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            
            if board[r][c] != word[i] or (r, c) in path:
                return
            
            path.append((r, c))
            backtrack(r + 1, c, i + 1)
            backtrack(r - 1, c, i + 1)
            backtrack(r, c+ 1, i + 1)
            backtrack(r, c - 1, i + 1)
            path.pop()

            
        for row in range(rows):
            for col in range(cols):
                backtrack(row, col, 0)
                path = []

        return res