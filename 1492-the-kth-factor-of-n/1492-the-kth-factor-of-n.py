class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        store=[]
        for i in range(1,n+1):
            if n%i==0:
                store.append(i)
        if len(store)<k:
            return -1
        return store[k-1]