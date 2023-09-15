class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        st1={}
        st2={}
        
        for inx,val in enumerate(list1):
            st1[val]=inx
        for inx,val in enumerate(list2):
            st2[val]=inx
        # print(st1)
        # print(st2)
        ans=defaultdict(list)
        minn=float('inf')
        for i in st1:
            if i in st2:
                temp=st1[i] + st2[i]
                if minn>=temp:
                    ans[temp].append(i)
        m=min(ans.keys())
        return ans[m]