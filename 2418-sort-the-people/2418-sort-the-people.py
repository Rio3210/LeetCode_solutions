class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        
        temp = sorted(heights, reverse = True)
        res = []
        for i in temp:
            res.append(names[heights.index(i)])
        return res