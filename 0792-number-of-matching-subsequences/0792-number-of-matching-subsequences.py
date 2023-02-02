class Solution:
    # def numMatchingSubseq(self, s: str, words: List[str]) -> int:
    #     c=Counter(words)            
    #     count=0
    #     for k in c:
    #         print(k)
    #         i = 0
    #         j = 0
    #         while(j < len(k) and i < len(s)):
    #             if(s[i] == k[j]):
    #                 i = i + 1
    #                 j = j + 1
    #             else:
    #                 i= i + 1
    #         if(j == len(k)):
    #             count+=c[k]                
    #     return count
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
    
        def is_sub(word):
            index=-1
            for ch in word:
                index=s.find(ch,index+1)
                if index==-1:
                    return False
            return True

        c=0
        for word in words:
            if is_sub(word):
                c+=1

        return c


                
        