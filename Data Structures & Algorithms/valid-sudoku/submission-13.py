class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        ## Checks each row 
        for i in range(9):
            tempSet = set()
            for j in range(9):
                if board[i][j] != "." and board[i][j] in tempSet:
                    return False
                else: 
                    tempSet.add(board[i][j])

        ## Checks each column
        for i in range(9):
            tempSet = set()
            for j in range(9):
                if board[j][i] != "." and board[j][i] in tempSet:
                    return False
                else: 
                    tempSet.add(board[j][i])
        
        ## Check each 3x3 box
        for starty in range(0, 9, 3):
            for startx in range(0, 9, 3):
                tempSet = set()
                for i in range(3):
                    for j in range(3):
                        if board[starty+j][startx+i] != "." and board[starty+j][startx+i] in tempSet:
                            return False
                        else: 
                            tempSet.add(board[starty+j][startx+i])
        return True