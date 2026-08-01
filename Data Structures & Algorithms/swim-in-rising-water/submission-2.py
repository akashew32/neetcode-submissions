class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ## Modified dijkstra
        n = len(grid)
        heap = []
        visited = [[False] * n for _ in range(n)]  
        visited[0][0] = True
        heapq.heappush(heap, (grid[0][0], 0, 0))
        def expand(prev, r, c):
            if r - 1 >= 0 and not visited[r - 1][c]:
                heapq.heappush(heap, (max(prev, grid[r-1][c]), r - 1, c))
                visited[r-1][c] = True
            if r + 1 < n and not visited[r + 1][c]:
                heapq.heappush(heap, (max(prev, grid[r+1][c]), r + 1, c))
                visited[r+1][c] = True
            if c - 1 >= 0 and not visited[r][c-1]:
                heapq.heappush(heap, (max(prev, grid[r][c-1]), r, c-1))
                visited[r][c-1] = True
            if c + 1 < n and not visited[r][c+1]:
                heapq.heappush(heap, (max(prev, grid[r][c+1]), r, c+1))
                visited[r][c+1] = True

            


        while heap:
            prev, r, c = heapq.heappop(heap)
            if r == n-1 and c == n - 1:
                return prev
            
            expand(prev, r, c)



