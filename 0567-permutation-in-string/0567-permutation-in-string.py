class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s1=sorted(s1)
        for i in range(len(s2)-len(s1)+1):
            s=""
            if s2[i] in s1:
                for j in range(i,len(s1)+i):
                    s+=s2[j]
                s=sorted(s)
                # print(s)
                if s==s1:
                    return True
        return False