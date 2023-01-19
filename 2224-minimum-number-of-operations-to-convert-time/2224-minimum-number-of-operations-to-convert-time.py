class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        
        
        
        
        
        
        crr=correct.split(':')
        curr=current.split(':')
        
        hr1=int(crr[0])*60 +int(crr[1])
        hr2= int(curr[0])*60 +int(curr[1])
        diff=hr1-hr2
        count=0
        for i in [60, 15, 5, 1]:
            count += diff // i 
            diff %= i 
        return count
        