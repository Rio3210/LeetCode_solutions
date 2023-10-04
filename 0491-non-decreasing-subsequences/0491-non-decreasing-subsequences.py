class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res={}
        seq=[]
        n=len(nums)
        def helper(idx):
            if len(seq)>1:
                res[tuple(seq)]=1
            for i in range(idx,n):
                if not seq or nums[i]>=seq[-1]:
                    seq.append(nums[i])
                    helper(i+1)
                    seq.pop()
        helper(0)
        return res.keys()