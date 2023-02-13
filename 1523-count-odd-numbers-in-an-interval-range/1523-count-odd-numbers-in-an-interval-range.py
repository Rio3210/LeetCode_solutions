class Solution:
    def countOdds(self, low: int, high: int) -> int:
        count=0
        print((high-low+1)//2)
        if (high-low + 1) %2==0 and high%2==0 and low%2==0:
            return (high-low+1)//2
        if (high-low + 1) %2==0 and low%2!=0 and high%2==0:
            return (high-low+1)//2
        if (high-low + 1) %2==0 and low%2==0 and high%2!=0:
            return (high-low+1)//2
        if (high-low + 1) %2==0:
            return ((high-low+1)//2)+1
        
        if low%2!=0 and high%2!=0:
            return ((high-low)//2)+1
        return (high-low)//2