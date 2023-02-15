class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        r1=0
        for i in num:
            r1=r1*10+i
        ans=[]
        for i in str(r1+k):
            ans.append(int(i))
        return ans