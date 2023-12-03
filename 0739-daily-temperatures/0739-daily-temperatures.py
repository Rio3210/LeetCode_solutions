class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans=[0]*len(temperatures)
        n=len(temperatures)
        stack=[]
        
        for i in range(n-1,-1,-1):
            while stack and temperatures[stack[-1]]<=temperatures[i]:
                stack.pop()
            if stack and temperatures[stack[-1]]>temperatures[i]:
                ans[i]=stack[-1]-i
            stack.append(i)
        return ans
    