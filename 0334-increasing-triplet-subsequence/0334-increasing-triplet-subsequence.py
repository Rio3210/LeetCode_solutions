class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        inc=[float('inf'),float('inf')]
        
        for i in nums:
            if i<=inc[0]:
                inc[0]=i
            elif i<=inc[1]:
                inc[1]=i
            else:
                return True
        return False