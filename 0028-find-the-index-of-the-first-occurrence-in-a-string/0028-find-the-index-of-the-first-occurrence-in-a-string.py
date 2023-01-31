class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        stack=[]
        if len(haystack)==0:
            return 0
        if len(haystack)<len(needle):
            return -1
        res=-1
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)]==needle:
                res=i
                break
        return res
            
        
        
            