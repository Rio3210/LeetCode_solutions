class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        count=[]
        for i,v in enumerate(mat):
            count.append((i,v.count(1)))
        
        srt=sorted(count,key=lambda x: x[1])
        ans=[]
        for i in srt[:k]:
            ans.append(i[0])
        return ans
            
            