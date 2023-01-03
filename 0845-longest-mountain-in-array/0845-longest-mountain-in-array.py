class Solution(object):
    def longestMountain(self, arr:List[int]):
        up= [0] * len(arr)
        down= [0] * len(arr)
        for i in range( len(arr)-1):
            if arr[i+1] > arr[i]:
                up[i+1] = up[i] + 1
                print(up[i+1])
         
        print(up)
        for i in range(len(arr) - 2,-1,-1):
            print(i)
            if arr[i] > arr[i + 1]: 
                  down[i] = down[i + 1] + 1

        maxx=0
        for u,d in zip(up,down):
            if u!=0 and d!=0:
                maxx=max(maxx,u+d+1)
        return maxx

       
        