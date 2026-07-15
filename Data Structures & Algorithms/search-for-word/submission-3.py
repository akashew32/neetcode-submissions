class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        visited = [[False] * cols for _ in range(rows)]
        res = False

        def backtrack(i, r, c):
            nonlocal res
            nonlocal rows
            nonlocal cols
            if (i >= len(word)):
                res = True
                return

            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            elif visited[r][c]:
                return
            elif word[i] != board[r][c]:
                return 
            else:
                visited[r][c] = True
                backtrack(i + 1, r + 1, c)
                backtrack(i + 1, r - 1, c)
                backtrack(i + 1, r, c + 1)
                backtrack(i + 1, r, c - 1)
                visited[r][c] = False

        for row in range(rows):
            for col in range(cols):
                i = 0
                backtrack(i, row, col)
        return res
