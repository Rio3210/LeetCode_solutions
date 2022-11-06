class Solution:
    def reverseVowels(self, s: str) -> str:
        s=list(s)
        vowles=['a','A','e','E','i','I','o','O','u','U']
        vowins=[c for c in s if c in vowles]
        m=vowins[::-1]
        for i in range(len(s)):
            if s[i] in vowles:
                s[i]=m.pop(0)
        return ''.join(s)
        
        # loc=[]
        # s=list(s)
        # for i in range(len(s)):
        #     if(s[i] in "aeiouAEIOU"):
        #         loc.append(i)
        # for i in range(len(loc)//2):
        #     s[loc[i]],s[loc[-i-1]]=s[loc[-i-1]],s[loc[i]]
        # return "".join(s)