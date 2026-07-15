class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = [[False] * n for _ in range(n)]
        path = 0
        q = deque()
        q.append((0, 0))
        flag = False
        while q:
            for i in range(len(q)):
                temp = q.popleft()
                r = temp[0]
                c = temp[1]
                if temp[0] >= n or temp[0] < 0 or temp[1] >= n or temp[1] < 0:
                    continue
                if visited[temp[0]][temp[1]]:
                    continue
                if grid[temp[0]][temp[1]]:
                    continue
                visited[temp[0]][temp[1]] = True
                q.append((r, c + 1))
                q.append((r, c - 1))
                q.append((r + 1, c))
                q.append((r - 1, c))
                q.append((r + 1, c + 1))
                q.append((r - 1, c + 1))
                q.append((r-1 , c- 1))
                q.append((r+1, c - 1))
                if temp == (n -1, n- 1):
                    flag = True
            path += 1
            if flag:
                break
        if not flag:
            return -1
        return path 