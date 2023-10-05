class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        
        def dist(p1,p2):
            x1,y1= p1[0],p1[1]
            x2,y2= p2[0],p2[1]
            
            x=(x2-x1)**2
            y=(y2-y1)**2
            return math.pow(x+y,0.5)
        
        D=[
        dist(p1,p2),
        dist(p1,p3),
        dist(p1,p4),
        dist(p2,p3),
        dist(p2,p4),
        dist(p3,p4)
        ]
        D.sort()
        return 0<D[0]==D[1]==D[2]==D[3] and D[4]==D[5]