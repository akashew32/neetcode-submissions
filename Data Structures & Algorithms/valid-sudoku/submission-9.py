class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        ## Checks each row 
        for i in range(9):
            currRow = board[i]
            tempSet = set()
            for num in currRow:
                if num != "." and num in tempSet:
                    return False
                else: 
                    tempSet.add(num)

        ## Checks each column
        for i in range(9):
            tempSet = set()
            for j in range(9):
                num = board[j][i]
                if num != "." and num in tempSet:
                    return False
                else: 
                    tempSet.add(num)
        
        ## Check each 3x3 box
        for starty in range(0, 9, 3):
            for startx in range(0, 9, 3):
                tempSet = set()
                for i in range(3):
                    for j in range(3):
                        num = board[starty+j][startx+i]
                        if num != "." and num in tempSet:
                            return False
                        else: 
                            tempSet.add(num)
        return True