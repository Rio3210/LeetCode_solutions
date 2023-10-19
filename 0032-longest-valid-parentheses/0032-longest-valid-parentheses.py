class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack=[]
        lst=[0]*len(s)
        if s=="":
            return 0
        
        for ind,sym in enumerate(s):
            if sym=="(":
                stack.append(ind)
            else:
                if stack:
                    lst[stack.pop()]=1
                    lst[ind]=1
        print(lst)
        l=0
        r=0
        maxx=float('-inf')
        temp=0
        for i in range(len(s)):
            if lst[i]==1:
                temp+=1
            else:
                maxx=max(maxx,temp)
                temp=0
        
        return max(temp,maxx)
#         while r<n:
            
#             maxx=(r-l+1,maxx)