class Solution:
    def totalNQueens(self, n: int) -> int:
        col=set()
        postive_diagonal=set()#r+c
        negative_diagonal=set()#r-c
        res=0
        def helper(r):
            if r==n:
                nonlocal res
                res+=1
                return
            for c in range(n):
                if c in col or r+c in postive_diagonal or r-c in negative_diagonal:
                    continue
                col.add(c)
                postive_diagonal.add(r+c)
                negative_diagonal.add(r-c)
                helper(r+1)
                col.remove(c)
                postive_diagonal.remove(r+c)
                negative_diagonal.remove(r-c)
        helper(0)
        return res