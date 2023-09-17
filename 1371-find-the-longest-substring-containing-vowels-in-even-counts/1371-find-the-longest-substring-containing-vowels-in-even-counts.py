class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels = {'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16}
        d = {0: -1} 
        state, ans = 0, 0 
        for i, c in enumerate(s): 
            if c in vowels:
                state ^= vowels[c]
            
            if not (state in d): 
                d[state] = i 
                
            ans = max(ans, i-d[state])
        
        return ans
        