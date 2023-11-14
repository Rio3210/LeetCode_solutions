class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        if len(s)==3:
            return 1 if s==s[::-1] else 0
        ans=0
        for letter in set(s):
            f=s.find(letter)
            sc=s.rfind(letter)
            # print(f,sc,letter)
            if f!=s:
                ans+=len(set(s[f+1:sc]))
        return ans
            