class Solution:
    def reverse(self, x: int) -> int:
        
        temp=0
        result=0
        sign=1
        if x<0:
            sign=-1
            x=x*sign
        while x>0:
            temp=x%10
            result=(result*10)+temp
            x=x//10
        if -2147483648<result<2147483648:          
            return result *sign
        else:
            return 0
        
    
     