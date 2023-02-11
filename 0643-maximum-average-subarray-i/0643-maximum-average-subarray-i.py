class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        count=0
        for i in range(k):
            count+=nums[i]
        z=[count]
        for j in range(k,len(nums)):
            count=count+nums[j]-nums[j-k]
            z.append(count)

        m=max(z)
        return m/k