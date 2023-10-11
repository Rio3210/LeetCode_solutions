class Solution:
    def sortVowels(self, s: str) -> str:
        vowels="AEIOUaeiou"
        res=""
        vow_in_s=sorted(filter(lambda x : x in vowels,s))
        
        for ch in s:
            if ch in vowels:
                res= res + vow_in_s.pop(0)
            else:
                res+=ch
        return res