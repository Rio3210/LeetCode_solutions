class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        dp = [grid[0][0] for _ in range(c)]
        for j in range(1, c):
            dp[j] = dp[j-1] + grid[0][j]
        for i in range(1, r):
            dp[0] += grid[i][0]
            for j in range(1, c):
                dp[j] = min(dp[j-1], dp[j]) + grid[i][j]
        return dp[-1]