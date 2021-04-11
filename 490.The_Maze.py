from collections import deque


class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        m, n, visited = len(maze), len(maze[0]), set()

        def dfs(x, y):
            if (x, y) not in visited:
                visited.add((x, y))
            else:
                return False
            if [x, y] == destination:
                return True
            # loop with L, R, U, D position
            for i, j in (0, -1), (0, 1), (-1, 0), (1, 0):
                new_X, new_Y = x, y
                while 0 <= new_X + i < m and 0 <= new_Y + j < n and maze[new_X + i][new_Y + j] != 1:
                    new_X += i
                    new_Y += j
                # run dfs recursive
                if dfs(new_X, new_Y):
                    return True
            return False
        return(dfs(*start))
