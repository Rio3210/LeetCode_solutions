class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dp=Counter(nums)
        print(dp)
        for i in range(len(nums)):
            if dp.get(nums[i])>1:
                return True
        return False
                