class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        @lru_cache
        def recur(start_x, start_y):
            if start_x >= m or start_y >= n:
                return 0
            if obstacleGrid[start_x][start_y] == 1:
                return 0
            if start_x == m - 1 and start_y == n - 1:
                return 1

            right = recur(start_x + 1, start_y)
            down = recur(start_x, start_y + 1)
            return right + down

        if obstacleGrid[0][0] == 1 or obstacleGrid[m - 1][n - 1] == 1:
            return 0

        return recur(0, 0)