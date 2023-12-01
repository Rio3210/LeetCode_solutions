class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        
        i = 0
        n=len(nums)
        while i < n:
            correct = nums[i] - 1
            if nums[i] != nums[correct]:

                nums[i], nums[correct] = nums[correct], nums[i]
            else:
                i += 1
        print(nums)
        ans=[]
        for i,num in enumerate(nums):
            if i!=num-1:
                ans.append(num)
        return ans
            

        