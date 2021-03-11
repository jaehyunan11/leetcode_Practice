class Solution:
    def maxKilledEnemies(self, grid)
       if not grid:
            return 0
        m = len(grid) # row
        n = len(grid[0]) # column
        row_count = [[0]*n for _ in range(m)]
        col_count = [[0]*n for _ in range(m)]

        # [0,0,0,0] -> number of enemies to (left, right, top, bottom)
        

        # left to right
        for i in range(n):

