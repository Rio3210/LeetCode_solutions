class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res=[]
        res.append(nums[0])
        maxx=res[0]
        for i in range(1,len(nums)):
            res.append(max(res[i-1]+nums[i],nums[i]))
            maxx=max(maxx,res[i])
        return maxx
        