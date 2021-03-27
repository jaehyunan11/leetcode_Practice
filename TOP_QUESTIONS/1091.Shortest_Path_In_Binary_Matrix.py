from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid):
        # # edge case
        # if grid[0][0] or grid[-1][-1] == 1:
        #     return -1

        # rows = len(grid)
        # cols = len(grid[0])
        # # 8 directionally path
        # directions = [(1, 0), (1, 1), (0, 1), (-1, 1),
        #               (-1, 0), (-1, -1), (0, -1), (1, -1)]
        # # row, col, step
        # queue = deque([(0, 0, 1)])

        # while queue:
        #     i, j, steps = queue.popleft()
        #     if (i, j) == (rows-1, cols-1):
        #         return steps
        #     for di, dj in directions:
        #         ii, jj = i+di, j+dj
        #         if 0 <= ii < rows and 0 <= jj < cols and not grid[ii][jj]:
        #             grid[ii][jj] = 1  # mark as visited
        #             queue.append((ii, jj, steps+1))
        # return -1

        if grid[0][0] or grid[-1][-1]:
            return -1
        rows, cols, q = len(grid), len(grid[0]), [(0, 0, 1)]
        while q:
            row, col, dist = q.pop(0)
            if row == rows-1 and col == cols-1:
                return dist
            for r, c in [(row-1, col-1), (row-1, col), (row-1, col+1), (row, col-1), (row, col+1), (row+1, col-1), (row+1, col), (row+1, col+1)]:
                if r >= 0 and r < rows and c >= 0 and c < cols and not grid[r][c]:
                    q.append((r, c, dist+1))
                    grid[r][c] = 1
        return -1


S = Solution()
grid = [[0, 1], [1, 0]]
print(S.shortestPathBinaryMatrix(grid))
