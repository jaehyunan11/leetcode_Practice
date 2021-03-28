class Solution:
    def numDistinctIslands(self, grid):
        """
        Iterate through grid
        - BFS where there is a 1
        - set its value to 0 then find neighbours and add to queue
        - for all other directions that are not 1, append some unquie char for nonvalid
        - when poping a value keep track of the direction it cam from 
        - Use set to keep unique ways bfs worked
        """

        if not grid:
            return 0

        def bfs(r, c):
            directions = [('r', 0, 1), ('d', 1, 0), ('l', 0, -1), ('u', -1, 0)]
            tempDir = ''
            queue = [('s', r, c)]
            # print(r, c)
            while queue:
                cell = queue.pop(0)
                # print(cell)
                fromDir = cell[0]
                tempDir += fromDir

                cellR = cell[1]
                cellC = cell[2]
                # print("currCell", cellR, cellC)

                for direction in directions:
                    newR = cellR + direction[1]
                    newC = cellC + direction[2]
                    # print("newPre", newR, newC)

                    # If newR and newC are within grid range and grid[newR][newC] is island then change to water (0)
                    if newR >= 0 and newR < len(grid) and newC >= 0 and newC < len(grid[0]) and grid[newR][newC] == 1:
                        grid[newR][newC] == 0
                        queue.append((direction[0], newR, newC))
                        # print("new", newR, newC)
                    else:
                        tempDir += "n"
            return tempDir

        # Create PatternSet
        # traverse the grid
        # if grid contains 1 then change to 0
        # check curr neighbor
        # Add it ot patternset.
        # If the pattern is same then it will be offset.
        # return length of patternset
        patternSet = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    grid[row][col] == 0
                    pattern = bfs(row, col)
                    print(pattern)
                    patternSet.add(pattern)
        return len(patternSet)


# S = Solution()
# grid = [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]]
# print(S.numDistinctIslands(grid))


class Solution2:
    def numDistinctIslands(self, grid):
        """
            Iterate through grid
            - BFS where there is a 1
            - set its value to 0 then find neighbours and add to queue
            - for all other directions that are not 1, append some unquie char for nonvalid
            - when poping a value keep track of the direction it cam from 
            - Use set to keep unique ways bfs worked
        """
        rows = len(grid)
        if rows == 0:
            return 0
        cols = len(grid[0])
        if cols == 0:
            return 0
        res = set()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    path = []
                    self.getPath(grid, i, j, rows, cols, path)
                    res.add("".join(path))

        return len(res)

    def getPath(self, grid, i, j, r, c, path):
        if i < 0 or j < 0 or i == r or j == c or grid[i][j] == 0:
            return
        # grid[i][j] is within grid and it is island which is 1
        # to avoid repeating search change to 0
        grid[i][j] = 0
        path.append("1")

        path.append("T")  # Go Top
        self.getPath(grid, i + 1, j, r, c, path)

        path.append("B")  # Go Bottom
        self.getPath(grid, i - 1, j, r, c, path)

        path.append("L")  # Go Left
        self.getPath(grid, i, j + 1, r, c, path)

        path.append("R")  # Go Right
        self.getPath(grid, i, j - 1, r, c, path)


S = Solution()
grid = [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]]
print(S.numDistinctIslands(grid))
