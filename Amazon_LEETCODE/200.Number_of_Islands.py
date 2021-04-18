class Solution:
    def numIslands(self, grid):
        # dfs method
        # Edge case
        if not grid:
            return 0
        num_islands = 0
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    num_islands += 1
        return num_islands

    def dfs(self, grid, r, c):
        # If out of grid then return 0
        if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == '0':
            return 0
        else:
            # Change to 0 Not to revisit
            grid[r][c] = '0'
            # DFS search U,D,R,L
            self.dfs(grid, r+1, c)  # Neighbor to Down
            self.dfs(grid, r-1, c)  # Neighbor to up
            self.dfs(grid, r, c+1)  # Neighbor to Right
            self.dfs(grid, r, c-1)  # Neighbor to lef

# Time: O(M×N) where M is the number of rows and N is the number of columns.
# Space: O(M×N) in case that the grid map is filled with lands where DFS goes by M×N deep.


S = Solution()
grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]
print(S.numIslands(grid))
