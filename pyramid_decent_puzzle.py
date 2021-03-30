def puzzleSolver(puzzle, target):
    # length of puzzle
    n = len(puzzle)
    # create queue
    queue = []
    # set first count
    count = 1
    # rows and colums start with (0,0)
    rows = cols = 0
    # Add first row, column, first num of puzzle, ''(empty string)
    queue.append([rows, cols, puzzle[0][0], ''])

    # loop queue until it is empty
    while queue:
        for i in range(len(queue)):
            # remove first in queue and assign to curr
            curr = queue.pop(0)
            # if count is same as length of puzzle then check curr num is same as target
            # if same then return the path
            if count == n:
                if curr[2] == target:
                    return curr[3]
            else:
                # Increase row index by 1 e.g. (1,0),(2,0)(3,0)
                next_row = curr[0] + 1
                next_col = curr[1]
                # Left path only if next_row is increased by 1 e.g. (+1, 0)
                # Multiply curr number in puzzle and new left side of num in puzzle
                queue.append([next_row, next_col, curr[2] *
                              puzzle[next_row][next_col], curr[3] + 'L'])
                # Right path if both next_row & next_col are increased by 1 e.g. (+1, +1)
                # Multiply curr number in puzzle and new right side of num in puzzle
                queue.append([next_row, next_col + 1, curr[2]
                              * puzzle[next_row][next_col + 1], curr[3] + 'R'])
        count += 1
    # if there is no return val in while loop and exited then there is no valid path.
    return 'There is no valid path'

# TIME : O(N) where n is length of puzzle
# Space : O(N) where n is length of puzzle


puzzle1 = [[2], [4, 3], [3, 2, 6], [2, 9, 5, 2], [10, 5, 2, 15, 5]]
target1 = 720
print(puzzleSolver(puzzle1, target1))
