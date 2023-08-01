class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def recur(x,n):
            if n==0:
                return 1
            elif n>0:
                if n%2==0:
                    return recur(x*x,n//2)
                else:
                    return x * recur(x,n-1)
            else:
                return recur(1/x,-n)
        return recur(x,n)