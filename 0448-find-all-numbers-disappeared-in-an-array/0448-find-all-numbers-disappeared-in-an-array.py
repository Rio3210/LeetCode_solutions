class Solution(object):
    def findDisappearedNumbers(self, nums):
        
        num_set=set(nums)
        list1=[]
        for i in range(1,len(nums)+1):
            if i not in num_set:
                list1.append(i)
        return list1
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        