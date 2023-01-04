class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        cot=Counter(tasks)
        print(cot.values())
        count=0
        for i in cot:
            if cot[i]==1:
                return -1
        
        for i in cot:
            
            count+=cot[i]//3+bool(cot[i]%3)    
            
        return count
        

                