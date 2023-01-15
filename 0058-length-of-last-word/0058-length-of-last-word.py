class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lis=s.split()
        return len(lis[len(lis)-1])
        
        
        