class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        # n=len(nums)
        # stack=[]
        # for i in range(2*n-1,-1,-1):
        #     num=nums[i%n]
        #     while stack and stack[-1]<=num:
        #         stack.pop(-1)
        #     if i<n:
        #         if len(stack)==0:
        #             nums[i]=-1
        #         else:
        #             nums[i]=stack[-1]
        #     stack.append(num)
        # return nums
        numm=nums+nums
        n=len(nums)
        result=[-1]*n
        for i in range(n):
            for j in range(i+1,len(numm)):
                if numm[j]>nums[i]:
                    result[i]=numm[j]
                    break
        return result