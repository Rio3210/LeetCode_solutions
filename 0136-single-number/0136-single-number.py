from collections import Counter
class Solution(object):
    def singleNumber(self, nums):
        
        unique=0
        for num in nums:
            unique ^=num
        return unique
            
            
        """
        :type nums: List[int]
        :rtype: int
        """
        