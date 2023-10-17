class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        valid_word = set(wordDict)
        ans = []
        n = len(s)

        def helper(s, temp, ss):
            nonlocal ans, n
            if not s:
                ans.append(' '.join(temp))
                return
            for j in range(1, len(s) + 1):
                if s[:j] in valid_word:
                    temp.append(s[:j])
                    helper(s[j:], temp, ss)
                    temp.pop()

        helper(s, [], set())
        return ans
                
            
            
        
            