class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        d = {}
        for word in words:
            d[word] = d.get(word, 0) + 1
        
        res = sorted(d, key=lambda word: (-d[word], word))
        return res[:k]