class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mn=float("inf")
        maxxdif=0
       
        for i in range(len(prices)):
            mn=min(prices[i],mn)
            maxxdif=max(prices[i]-mn,maxxdif)
        return maxxdif
            
        
                
                
                