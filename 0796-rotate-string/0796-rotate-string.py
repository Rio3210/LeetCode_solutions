class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        
        n=len(s)
        s=list(s)
        for i in range(n):
            if ''.join(s)==goal:
                return True
            for j in range(n-1):
                s[j],s[j+1]=s[j+1],s[j]
        return False