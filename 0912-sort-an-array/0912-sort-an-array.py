class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        heapq.heapify(nums)
        n=len(nums)
        ans=[]
        for i in range(n):
            ans.append(heapq.heappop(nums))
        return ans
            
        