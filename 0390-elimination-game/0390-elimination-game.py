class Solution:
    def lastRemaining(self, n: int) -> int:
        head = 1 
        step = 1 
        fwd = True
        while n>1:
            if fwd or n%2!=0:
                head+=step
            step=step * 2
            n=n//2
            fwd= not fwd
        return head