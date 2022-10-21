class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        
        hashmap = {}
        
        for i in range(len(nums)):
            if nums[i] in hashmap and abs(hashmap[nums[i]]-i) <= k:
                return True
            hashmap[nums[i]] = i
        
        return False
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        