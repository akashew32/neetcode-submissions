class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = [[False] * cols for _ in range(rows)]
        area = 0

        def dfs(row, col) -> int:
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return 0
            if visited[row][col]:
                return 0
            if grid[row][col] == 0:
                return 0
            visited[row][col] = True
            return 1 + dfs(row - 1, col) + dfs(row + 1, col) + dfs(row, col + 1) + dfs(row, col - 1)

        for row in range(rows):
            for col in range(cols):
                if not visited[row][col] and grid[row][col] == 1:
                    area = max(area, dfs(row, col))
        return area
