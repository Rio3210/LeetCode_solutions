class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n=len(nums)
        check=[True]*n
        sor=sorted(nums)
        for i in range(n):
            if sor[i]!=nums[i]:
                check[i]=False
        # print(check)
        l=0
        if sor==nums:
            return 0
        for i in range(n):
            if check[i]==False:
                l=i
                break
        r=n-1
        for j in range(n-1,-1,-1):
            if check[j]==False:
                r=j
                break
        return r-l+1
                
            
        
            
            