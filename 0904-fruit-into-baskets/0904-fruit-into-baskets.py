class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket={}
        winstart=0
        maxFruits=0
        for i in range(len(fruits)):
            currFruit=fruits[i]
            if currFruit not in basket:
                basket[currFruit] = 0 
            basket[currFruit] += 1
            
            while len(basket)>2:
                remove=fruits[winstart]
                basket[remove] -= 1 
                if basket[remove] == 0:
                    del basket[remove] 
                winstart += 1        
            maxFruits = max(maxFruits, i - winstart + 1)  
        return maxFruits
                
        
                
        
        