class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            visited=set()
            for col in row:
                if col!='.' and col in visited:
                    return False
                visited.add(col)
        n=len(board)
        for col in range(n):
            visited=set()
            for row in board:
                if row[col]!='.' and row[col] in visited:
                    return False
                visited.add(row[col])
        for row3 in range(0,9,3):
            for col3 in range(0,9,3):
                visited=set()
                for row in range(row3,row3+3):
                    for col in range(col3,col3+3):
                        if board[row][col]!='.' and board[row][col] in visited:
                            return False
                        visited.add(board[row][col])
        return True
    
    