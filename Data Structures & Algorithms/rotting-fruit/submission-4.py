class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        visited = []

        rows = len(grid)
        cols = len(grid[0])
        visited = [[False] * cols for _ in range(rows)]

        steps = 0

        for row in range(rows):
            for col in range(cols):
                if not grid[row][col]:
                    visited[row][col] = True
                elif grid[row][col] == 2:
                    visited[row][col] = True
                    q.append((row, col))
        def check(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return
            if visited[row][col]:
                return
            visited[row][col] = True
            q.append((row, col))



        while q:
            for i in range(len(q)):
                curr = q.popleft()
                r = curr[0]
                c = curr[1]
                check(r + 1, c)
                check(r - 1, c)
                check(r, c + 1)
                check(r, c - 1)
            steps += 1
        
        for row in range(rows):
            for col in range(cols):
                if not visited[row][col]:
                    return -1
        print(steps)
        return max(0, steps - 1)