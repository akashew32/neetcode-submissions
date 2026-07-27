class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left = 0
        right = len(matrix[0]) - 1
        top = 0
        bottom = len(matrix) - 1
        dir = 0
        res = []

        while left <= right and top <= bottom:
            if dir == 0:
                for c in range(left, right + 1):
                    res.append(matrix[top][c])
                top += 1
                dir += 1
            elif dir == 1:
                for r in range(top, bottom + 1):
                    res.append(matrix[r][right])
                right -= 1
                dir += 1
            elif dir == 2:
                for c in range(right, left - 1, -1):
                    res.append(matrix[bottom][c])
                bottom -= 1
                dir += 1
            elif dir == 3:
                for r in range(bottom, top - 1, -1):
                    res.append(matrix[r][left])
                left += 1
                dir += 1

            dir = dir % 4
        return res
            