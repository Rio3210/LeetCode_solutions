class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        prefix_sums = [i for i in nums]
        suffix_sums = [i for i in nums]

        for i in range(1,len(nums)):
            prefix_sums[i] = prefix_sums[i-1]+nums[i]
        
        for i in range(len(nums)-2,-1,-1):
            suffix_sums[i] = suffix_sums[i+1]+nums[i]
        
        for i in range(len(nums)):
            nums[i] = (nums[i] * i - prefix_sums[i]) + suffix_sums[i] - nums[i] * (len(nums)-i-1)

        return nums
        