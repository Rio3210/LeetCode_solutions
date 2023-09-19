class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        cnt=0
        k=len(pref)
        for word in words:
            if word[:k]==pref:
                cnt+=1
        return cnt