class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Define a helper function to perform DFS traversal
        def dfs_traverse(grid, i, j):
            # Mark the current cell as visited by changing its value to '0'
            grid[i][j] = '0'
            # Check the neighboring cells and recursively traverse them if they are part of the island
            if i > 0 and grid[i-1][j] == '1':
                dfs_traverse(grid, i-1, j)
            if i < len(grid)-1 and grid[i+1][j] == '1':
                dfs_traverse(grid, i+1, j)
            if j > 0 and grid[i][j-1] == '1':
                dfs_traverse(grid, i, j-1)
            if j < len(grid[0])-1 and grid[i][j+1] == '1':
                dfs_traverse(grid, i, j+1)
        
        # Initialize a variable to keep track of the number of islands
        num_islands = 0
        # Traverse the entire grid and perform DFS traversal on each unvisited cell that is part of an island
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs_traverse(grid, i, j)
                    num_islands += 1
        # Return the total number of islands
        return num_islands