class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        st=sentence.split()
        d=set(dictionary)
        ans=[]
        for w in st:
            flag=False
            for i in range(len(w)):
                sub=w[:i+1]
                if sub in d:
                    ans.append(sub)
                    flag=True
                    break
            if flag==False:
                ans.append(w)
        # print(ans)
        return " ".join(ans)