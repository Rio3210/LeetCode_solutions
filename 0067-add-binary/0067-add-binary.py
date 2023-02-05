class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if a=='0' and b=='0':
            return '0'
        def convert_num(st):       
            val=0
            # st=st[::-1]
            for i in range(len(st)):
                val+=int(st[len(st)-1-i])*2**i
            
#                 if st[i]=='1':
#                     val+=2**i
            return val
        res=""
        summ=convert_num(a)+convert_num(b)
        while summ>0:
            rem=summ%2
            res+=str(rem)
            summ=summ//2
        return res[::-1]
        
                
                