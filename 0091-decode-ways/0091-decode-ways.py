class Solution:
    def numDecodings(self, s: str) -> int:
        dp={len(s):1}
        res=0
        def helper(i):
            nonlocal res
            if i in dp:
                return dp[i]
            if s[i]=="0":
                return 0
            res+=helper(i+1)
            # check if the number start with 1 and if the number starts with 2 (in this case we only can take digits of s between 0-6)
            if i+1<len(s) and (s[i]=="1" or s[i]=="2" and s[i+1] in "0123456"):
                res+=helper(i+2)
            dp[i]=res
            return res
        return helper(0)