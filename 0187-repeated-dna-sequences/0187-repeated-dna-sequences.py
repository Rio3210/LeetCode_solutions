class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        # print(len(s)-10)
        # print(s[22:])
        compare={}
        for i in range(len(s)-9):
            if s[i:i+10] in compare:
                compare[ s[i:i+10] ]+=1
            else:
                compare[s[i:i+10]]=1
        ans=[]
        for i in compare:
            if compare[i]>1:
                ans.append(i)
        return ans