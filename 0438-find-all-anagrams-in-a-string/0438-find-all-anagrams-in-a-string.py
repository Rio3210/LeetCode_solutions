class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res=[]
        sl=len(s)
        pl=len(p)
        cs=Counter(s[:pl])
        cp=Counter(p)
        # if cs==cp:res.append(0)
        
        for i in range(sl-pl+1):
            cs=Counter(s[i:pl+i])
            if cs==cp:
                res.append(i)
        return res