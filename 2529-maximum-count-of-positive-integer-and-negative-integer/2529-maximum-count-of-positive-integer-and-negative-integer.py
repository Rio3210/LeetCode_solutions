class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        count=0
        cnt=0
        for i in nums:
            if i<0:
                count+=1
        for i in nums:
            if i>0:
                cnt+=1
        return max(count,cnt)
                