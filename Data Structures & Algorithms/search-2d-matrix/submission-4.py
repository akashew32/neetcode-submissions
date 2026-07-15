class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lowerBound = 0;
        upperBound = len(matrix) - 1
        if matrix[0][0] == target:
            return True
        while upperBound != lowerBound:
            midBound = (upperBound + lowerBound) // 2
            if matrix[midBound][0] <= target <= matrix[midBound][-1]:
                upperBound = midBound
                lowerBound = midBound
            elif matrix[midBound][0] > target:
                upperBound = midBound
            else:
                lowerBound = midBound + 1
        row = upperBound
        lowerBound = 0
        upperBound = len(matrix[row])-1

        while upperBound != lowerBound:
            midBound = (upperBound + lowerBound) // 2
            if matrix[row][midBound] == target:
                return True
            elif matrix[row][midBound] > target:
                upperBound = midBound
            else:
                lowerBound = midBound + 1
        if lowerBound == upperBound:
            return matrix[row][lowerBound] == target
        return False