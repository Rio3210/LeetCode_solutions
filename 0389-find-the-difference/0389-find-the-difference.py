class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sc=Counter(s)
        tc=Counter(t)
        # print(tc)
        # print(sc)
        res=tc-sc
        
        for i,j in res.items():
            if j==1:
                return i
            