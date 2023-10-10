class Solution:
    def minOperations(self, nums: List[int]) -> int:
        sn = sorted(set(nums))
        n = len(nums)
        result = float('inf')
        
        for i in range(len(sn)):
            target = sn[i] + n - 1
            index = self.find_index(sn, target)
            count = n - (index - i)
            result = min(result, count)
        
        return result
    
    def find_index(self, arr, target):
        left = 0
        right = len(arr) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        
        return left