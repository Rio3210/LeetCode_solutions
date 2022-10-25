class Solution(object):
    def majorityElement(self, nums):
        
        hashmap={}
        for num in nums:
            if num not in hashmap:
                hashmap[num]=0
            hashmap[num]+=1
        for i in hashmap:
            if hashmap[i]>(len(nums)//2):
                return i
            
        """
        :type nums: List[int]
        :rtype: int
        """
        