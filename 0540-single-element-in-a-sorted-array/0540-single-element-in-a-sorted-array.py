class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # low,high=0,len(nums)-1
        # while low<high:
        #     mid=(low+high)//2
        #     if mid%2==1:
        #         mid-=1
        #     elif nums[mid]==nums[mid+1]:
        #         low=mid+2
        #     else:
        #         end=mid
        # return nums[low]
        
        c=Counter(nums)
        print(c)
        
        for i in c:
            if c[i]==1:
                return i