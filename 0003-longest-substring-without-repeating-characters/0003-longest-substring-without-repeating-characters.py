class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res={}
        l,r=0,0
        h=0
        while(r!=len(s)):
            if(s[r] in res):
                l+=1
                r=l
                res.clear()
            res[s[r]]=1
            h=max(h,r-l+1)
            r+=1
        return h