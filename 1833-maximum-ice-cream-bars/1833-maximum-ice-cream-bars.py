class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        count=0
        sumt=0
        n=sorted(costs,reverse=False)
        if n[0]>coins:
            return 0
        for i in range(len(n)):
            
            if sumt<coins and coins-sumt>=n[i]:
                sumt+=n[i]
                count+=1
        return count
            
        