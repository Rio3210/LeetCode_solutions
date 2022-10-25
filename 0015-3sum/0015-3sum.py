class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort() 
        triplets = []
        
        for i in range(len(nums)):
            if i > 0 and nums[i - 1] == nums[i]:
                continue 
                
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                curSum = nums[i] + nums[left] + nums[right]
                if curSum == 0:
                    triplets.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1;
                    
                    while left < right and nums[left - 1] == nums[left]:
                        left += 1
                    while left < right and nums[right + 1] == nums[right]:
                        right -= 1
                elif curSum < 0:
                    left += 1 
                else:
                    right -= 1 
        return triplets