class Solution:
    def numDistinctIslands(self, grid):
        # TIME: O(M * N)
        # SPACE : O(M * N) res M * N memory

        #         # Do a DFS to find all cells in the current island.
        def dfs(row, col, direction):
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
                return
            if (row, col) in seen or not grid[row][col]:
                return
            seen.add((row, col))
            path.append(direction)
            dfs(row+1, col, 'D')
            dfs(row-1, col, 'U')
            dfs(row, col+1, 'R')
            dfs(row, col-1, 'L')
            path.append('0')

        # repeatedly start DFS's as long as there are islands remaining.
        seen = set()
        unique_islands = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                path = []
                dfs(row, col, "0")
                if path:
                    unique_islands.add(tuple(path))

        return len(unique_islands)


S = Solution()
grid = [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]]
print(S.numDistinctIslands(grid))
