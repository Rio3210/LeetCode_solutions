class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        store=[]
        for i in range(1,n+1):
            store.append(str(i))
        store=sorted(store)
        ans=[]
        for j in range(n):
            ans.append(int(store[j]))
        return ans
            