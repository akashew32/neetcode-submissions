class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        visited = [[False] * cols for _ in range(rows)]  
        
        def floodfill(row, col, flag):
            if row >= rows or row < 0 or col >= cols or col < 0:
                return 
            if visited[row][col]:
                return
            if board[row][col] == "X":
                return
            visited[row][col] = True
            if flag:
                board[row][col] = "X"

            floodfill(row + 1, col, flag)
            floodfill(row - 1, col, flag)
            floodfill(row, col + 1, flag)
            floodfill(row, col - 1, flag)
        
        for col in range(cols):
            floodfill(0, col, False)
            floodfill(rows-1, col, False)
        for row in range(rows):
            floodfill(row, 0, False)
            floodfill(row, cols - 1, False)
        
        for row in range(rows):
            for col in range(cols):
                floodfill(row, col, True)
            
