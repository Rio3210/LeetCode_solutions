class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        
        list1=[]
        for _, c in sorted(zip(heights, names), reverse=True):
            list1.append(c)
        return list1