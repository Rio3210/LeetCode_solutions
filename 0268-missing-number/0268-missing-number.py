class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)+1
        summ=(n*(n-1))/2
        inner=0
        for i in range(len(nums)):
            inner+=nums[i]
        return int(summ-inner)