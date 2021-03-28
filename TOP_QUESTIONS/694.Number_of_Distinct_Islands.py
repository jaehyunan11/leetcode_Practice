class Solution:
    def numDistinctIsland(self, grid):
        # shape of island same then they are same island
        # unique or distant -> set

        # X 'start'
        # O 'Out of bound'
        # U 'Up' , R 'Right', L 'Left', D 'Down'

        # grid is empty return 0
        if grid == None or len(grid) == 0:
            return 0

        # grid rows and cols
        rows, cols = len(grid), len(grid[0])

        # shapes
        shapes = set()

        # visited
        visited = set()

        for i in range(rows):
            for j in range(cols):
                shape = set()
                if grid[i][j] == 1:
