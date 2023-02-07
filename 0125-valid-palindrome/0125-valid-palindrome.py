import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        res=re.sub(r'[^\w\s]','',s)
        res=res.replace('_','')
        final=res.replace(' ','').lower()[::-1]
        print(final)
        return final==final[::-1]