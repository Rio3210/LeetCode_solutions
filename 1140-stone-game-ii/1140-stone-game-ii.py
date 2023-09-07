class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        @lru_cache(None)
        def fn(i, m):
            """Return the net stones one could get at position i with m"""
            if len(piles) - i <= 2*m: return sum(piles[i:])
            return max(sum(piles[i:i+j])-fn(i+j, max(m, j)) for j in range(1, 2*m+1))
        
        return (fn(0, 1) + sum(piles))//2