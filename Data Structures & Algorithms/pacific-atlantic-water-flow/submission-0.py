class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()
        res = []

        def dfs(r, c, prev, ocean):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r, c) in ocean:
                return
            
            if heights[r][c] < prev:
                return
            
            ocean.add((r, c))
            dfs(r + 1, c, heights[r][c], ocean)
            dfs(r - 1, c, heights[r][c], ocean)
            dfs(r, c + 1, heights[r][c], ocean)
            dfs(r, c - 1, heights[r][c], ocean)
        
        for r in range(ROWS):
            dfs(r, 0, heights[r][0], pac)
            dfs(r, COLS - 1, heights[r][COLS - 1], atl)
        
        for c in range(COLS):
            dfs(0, c, heights[0][c], pac)
            dfs(ROWS - 1, c, heights[ROWS - 1][c], atl)
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in atl and (r, c) in pac:
                    res.append([r, c])
        return res




            
