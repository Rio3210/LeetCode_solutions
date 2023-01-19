class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        
        l, r = 0, 1
        
        while r < len(nums): 
            if nums[l] != 0:
                l+=1
            if nums[l] == 0 and nums[r] !=0:
                temp = nums[l]
                nums[l] = nums[r]
                nums[r] = temp
            r+=1
        """
        Do not return anything, modify nums in-place instead.
        """
        