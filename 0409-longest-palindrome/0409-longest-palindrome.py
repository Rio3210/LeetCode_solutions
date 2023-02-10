class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(s)==1:
            return 1
        count=Counter(s)
        
        odd=0
        res=[]
        for fre in count.values():
            res.append(fre)
            if fre % 2 != 0:
                odd += 1     
        if odd != 0:
            return sum(res) - odd + 1        
        elif odd == 0:
            return sum(res) 
            