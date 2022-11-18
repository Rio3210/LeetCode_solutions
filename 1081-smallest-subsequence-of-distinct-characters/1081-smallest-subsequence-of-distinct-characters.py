class Solution:
    def smallestSubsequence(self, s: str) -> str:
        ls={}
        for i, ch in enumerate(s):
            ls[ch]=i
        res=[]
        for ind, ch in enumerate(s):
            if ch not in res:
                while res and ch<res[-1] and ind <ls[res[-1]]:
                    res.pop()
                res.append(ch)
        
        return ''.join(res)
