class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        n=len(nums)
        stack=[]

        for i in range(2*n-1,-1,-1):
            num=nums[i%n]
            index=i+1

            while stack and stack[-1]<=num:
                stack.pop(-1)

            if i<n:
                if len(stack)==0:
                    nums[i]=-1

                else:
                    nums[i]=stack[-1]

            stack.append(num)

        return nums