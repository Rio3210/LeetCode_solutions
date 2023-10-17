class Solution:
    def longestWord(self, words: List[str]) -> str:
        
        words.sort()  
        valid_words=set()
        longest_word=""
        
        for word in words:
            pref=word[:-1]
            if pref=="" or pref in valid_words:
                valid_words.add(word)
                if len(word)>len(longest_word):
                    longest_word=word
        return longest_word
        
        