class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # return True
        cache={}
        def helper(l,r):
            if l>r:
                return 0
            if (l,r) in cache:
                return cache[(l,r)]
            evn= True if r %2 ==0 else 0
            
            left= piles[l] if evn else 0
            right = piles[r] if evn else 0 
            
            cache[(l,r)]=max( helper(l+1,r)+ left, helper(l,r-1)+right)
            return cache[(l,r)]
        return helper(0,len(piles)-1) > sum(piles)//2