class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        islands = 0
        ## Intialize an array for visited nodes
        visited = [[False] * cols for _ in range(rows)]    


        def dfs(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return
            if visited[row][col]:
                return
            if grid[row][col] == "0":
                return
            visited[row][col] = True
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        for row in range(rows):
            for col in range(cols):
                if not visited[row][col] and grid[row][col] == "1":   
                    dfs(row, col)
                    print(row, col)
                    islands += 1
        
        return islands
                    
