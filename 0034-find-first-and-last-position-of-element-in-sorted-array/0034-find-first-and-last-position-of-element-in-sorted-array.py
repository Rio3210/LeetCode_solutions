class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        stack=[]
        if target not in nums:
            return [-1,-1]
        for i in range(len(nums)):
            if nums[i]==target:
                stack.append(i)
                break
        for j in reversed(range(len(nums))):
            if nums[j]==target:
                stack.append(j)
                break
        return stack
               