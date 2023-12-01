class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        
        ans,count=0,0
        length=len(arr)
        for i in range(length):
            
            if i>=2 and (arr[i-2]<arr[i-1]>arr[i] or arr[i-2]>arr[i-1]<arr[i]):
                count+=1
            elif i>=1 and arr[i-1]!=arr[i]:
                count=2
            else:
                count=1
            ans=max(ans,count)
        return ans
                
        
        
