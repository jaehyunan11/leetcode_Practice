from collections import deque

class Solution2:
    def numsIsLands(self, grid):
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        num_islands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    q = deque([(i, j)])
                    grid[i][j] = '0'
                    while q:
                        x, y = q.popleft()
                        # navigate dx, dy in Down, Up, Right Left
                        for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
                            xx, yy = x+dx, y+dy
                            print(f"xx:{xx}, yy:{yy}")
                            if 0 <= xx < m and 0 <= yy < n and grid[xx][yy] == '1':
                                q.append((xx, yy))
                                grid[xx][yy] = '0'
                    num_islands += 1
        return num_islands


S2 = Solution2()
grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]
print(S2.numsIsLands(grid))
