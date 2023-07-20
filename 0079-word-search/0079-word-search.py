class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        Row,Col=len(board),len(board[0])
        visited=set()
        def dfs(r,c,i):
            if i==len(word):
                return True
            if (r<0 or c<0 or 
               r>=Row or c>=Col or 
                word[i]!= board[r][c] or
               (r,c) in visited ):
                return False
            
            visited.add((r,c))
            res=(dfs(r+1,c,i+1) or
                dfs(r-1,c,i+1)or
                dfs(r,c+1,i+1)or 
                dfs(r,c-1,i+1))
            visited.remove((r,c))
            return res
        
        for row in range(Row):
            for col in range(Col):
                if dfs(row,col,0):
                    return True
        return False
                
            