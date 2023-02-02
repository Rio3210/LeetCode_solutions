class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        c=Counter(words)
        # print(c)
       
        count=0
        for k in c:
            print(k)
            i = 0
            j = 0
            while(j < len(k) and i < len(s)):
                if(s[i] == k[j]):
                    i = i + 1
                    j = j + 1
                else:
                    i= i + 1
            if(j == len(k)):
                count+=c[k]
                print(c[k])
        return count


                
        