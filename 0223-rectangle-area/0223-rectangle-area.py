class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        first_area=abs(ax2-ax1)*abs(ay2-ay1)
        second_area=abs(bx2-bx1)*abs(by2-by1)
        
        if (bx1<ax2) and (ax1<bx2) and (by1<ay2) and (ay1<by2):
            r1=max(ax1,bx1)
            r2=min(ax2,bx2)
            r3=max(ay1,by1)
            r4=min(ay2,by2)
            return first_area +second_area - abs(r1-r2)*abs(r3-r4)
        return first_area +second_area