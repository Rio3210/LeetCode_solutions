class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        if not s:
            return ""
        res = ""
        for i in range(len(s)):
            p1 = self.isPalindrome(s, i, i)
            p2 = self.isPalindrome(s, i, i + 1)
            if len(p1) > len(res):
                res = p1
            if len(p2) > len(res):
                res = p2
        return res
        
    def isPalindrome(self, s, l, r):
        while (l >= 0 and r < len(s) and s[l] == s[r]):
            l -= 1
            r += 1
        return s[l+1:r]