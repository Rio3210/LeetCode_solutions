class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        result={0:-1}
        preSum=0
        for i in range(len(nums)):
            preSum+=nums[i]
            rem=preSum%k
            if rem in result:
                if i-result[rem]>1:
                    return True
            else:
                result[rem]=i
        return False
        