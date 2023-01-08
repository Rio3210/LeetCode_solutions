class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
        if len(points)<=2: return len(points)

        def slope(p1,p2):
            # Vertical line
            if p2[0]-p1[0] == 0:
                return inf
            return (p2[1]-p1[1]) / (p2[0]-p1[0])                

        res = 0
        for i in range(len(points)):
            count = defaultdict(int)
            for j in range(i+1,len(points)):
                count[slope(points[i],points[j])] += 1
            if count:
                res = max(res,max(count.values()))
        
        return res + 1
    
    
        
#         list1={}
#         count=0
#         def calcslope(y2,x2,y1,x1):
#             if x2-x1:
#                 return inf
#             return (y2-y1)/(x2-x1)
#         for i in range(len(points)-1):
#             for j in range(i+1,len(points)):
                
#                 m=calcslope(points[j][1],points[j][0],points[i][1],points[i][0])
#                 print(m)
#                 if m in list1:
#                     list1[m]+=1
#                 else:
#                     list1[m]=1
#         for i in list1:
#             count=max(list1[i],count)
#         return count
            