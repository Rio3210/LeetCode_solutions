class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        left=0
        right=n-1
        
        maxx=0
        while left<right:
            lh=height[left]
            rh=height[right]
            width=right-left
            h=min(lh,rh)
            maxx=max(maxx,width * h)
            
            if lh<rh:
                left+=1
            else:
                right-=1
        return maxx