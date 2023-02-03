class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s=""
        for i in digits:
            s+=str(i)
        res=int(s)+1
        stack=[int(x) for x in str(res)]
        return stack
        
            