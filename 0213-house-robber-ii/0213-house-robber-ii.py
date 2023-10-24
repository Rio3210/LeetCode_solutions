class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        def helper(nums):
            summ1,summ2=0,0
            for num in nums:
                temp=max(summ1+num,summ2)
                summ1=summ2
                summ2=temp
            return summ2
        return max(helper(nums[1:]),helper(nums[:-1]))