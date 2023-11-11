class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        
        def helper(sub):
            for i in range(len(sub)):
                if sub[i].lower() not in sub or sub[i].upper() not in sub:
                    return False
            return True
        # print(helper("zaAay"))
        n=len(s)
        long=""
        for i in range(n):
            for j in range(i+1,n+1):
                sub=s[i:j]
                if helper(sub) and len(sub)>len(long):
                    long=sub
        return long
        
            