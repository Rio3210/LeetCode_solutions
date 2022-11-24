class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        num=sorted(nums,reverse=True)
        return num[k-1]
        