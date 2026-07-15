class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        rows = len(grid)
        cols = len(grid[0])
        visited = [[False] * cols for _ in range(rows)]    

        def check(row, col, dist) -> bool:
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return False
            if visited[row][col]:
                return False
            
            grid[row][col] = min(grid[row][col], dist)
            visited[row][col] = True
            return True

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    q.append((row, col, 0))
                if grid[row][col] == -1:
                    visited[row][col] = True
        while q:
            temp = q.popleft()
            r = temp[0]
            c = temp[1]
            dist = temp[2]
            
            flag = check(r, c, dist)
            if flag:
                q.append((r + 1, c, dist + 1))
                q.append((r - 1, c, dist + 1))
                q.append((r, c + 1, dist + 1))
                q.append((r, c - 1, dist + 1))  

            

