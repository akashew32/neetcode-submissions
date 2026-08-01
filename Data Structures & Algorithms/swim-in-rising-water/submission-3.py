class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ## Modified dijkstra
        n = len(grid)
        heap = []
        visited = [[False] * n for _ in range(n)]  
        heapq.heappush(heap, (grid[0][0], 0, 0))
        def expand(prev, r, c):
            if r - 1 >= 0 and not visited[r - 1][c]:
                heapq.heappush(heap, (max(prev, grid[r-1][c]), r - 1, c))
            if r + 1 < n and not visited[r + 1][c]:
                heapq.heappush(heap, (max(prev, grid[r+1][c]), r + 1, c))
            if c - 1 >= 0 and not visited[r][c-1]:
                heapq.heappush(heap, (max(prev, grid[r][c-1]), r, c-1))
            if c + 1 < n and not visited[r][c+1]:
                heapq.heappush(heap, (max(prev, grid[r][c+1]), r, c+1))

            


        while heap:
            prev, r, c = heapq.heappop(heap)
            
            if r == n-1 and c == n - 1:
                return prev
            if visited[r][c]:
                continue
            visited[r][c] = True
            
            expand(prev, r, c)



