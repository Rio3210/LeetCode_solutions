class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        
        d=set()
        for ind,val in enumerate(fronts):
            if backs[ind]==val:
                d.add(val)
        minn=float("inf")
        for num in fronts + backs:
            if num not in d:
                minn=min(minn,num)
        return 0 if minn==float("inf") else minn
        
            
        
        
        
        
        # for num in fronts:
        #     if num not in b:
        #         store.append(num)
        # for n in backs:
        #     if n not in f:
        #         store.append(n)
        # if len(store)==0:
        #     return 0
        # return min(store)
    