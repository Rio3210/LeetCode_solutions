class Solution:
    def maxProduct(self, words: List[str]) -> int:
        maxx=0
        n=len(words)
        for i in range(n-1):
            temp=len(words[i])
            for l in range(i+1,n):
                nn=len(words[l])
                for ch in words[l]:
                    if ch in words[i]:
                        nn=0
                        break
                maxx=max(maxx,temp * nn)
        return maxx