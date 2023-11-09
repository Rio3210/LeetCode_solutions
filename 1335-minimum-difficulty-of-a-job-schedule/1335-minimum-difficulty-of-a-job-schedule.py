class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        
        @lru_cache(None)
        def dfs(ind, rem):
            if rem == 0:
                if ind == n:
                    return 0
                else:
                    return float('inf')
            if ind == n:
                return float('inf')
            
            maxx = float('inf')
            currMax = 0
            for i in range(ind, n):
                currMax = max(currMax, jobDifficulty[i])
                maxx = min(maxx, currMax + dfs(i + 1, rem - 1))
            
            return maxx
        
        if n < d:
            return -1
        
        return dfs(0, d)