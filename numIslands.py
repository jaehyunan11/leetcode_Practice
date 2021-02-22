class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0

        numIslands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    numIslands += 1
        return numIslands

    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == '0':
            return 0
        else:
            grid[i][j] = '0'
            self.dfs(grid, i+1, j)  # Neighbor to Down
            self.dfs(grid, i-1, j)  # Neighbor to Up
            self.dfs(grid, i, j+1)  # Neighbor to right
            self.dfs(grid, i, j-1)  # Neighbor to left


s = Solution()
grid = [["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]]

grid2 = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]
print(s.numIslands(grid))
print(s.numIslands(grid2))
