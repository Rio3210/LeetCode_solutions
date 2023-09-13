class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp=[[float('inf')] * (len(word2)+1) for i in range(len(word1)+1)]
        
        for i in range(len(word2)+1):
            dp[len(word1)][i]=len(word2)-i
        for j in range(len(word1)+1):
            dp[j][len(word2)]=len(word1)-j
        
        for k in range(len(word1)-1,-1,-1):
            for m in range(len(word2)-1,-1,-1):
                if word1[k]==word2[m]:
                    dp[k][m]=dp[k+1][m+1]
                else:
                    dp[k][m]=1 + min(dp[k+1][m],dp[k][m+1],dp[k+1][m+1])
        return dp[0][0]