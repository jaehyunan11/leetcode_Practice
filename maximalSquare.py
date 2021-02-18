class Solution:
    def __init__(self, matrix):
        self.matrix = matrix

    def maximalSquare(matrix):
        if not matrix:
            return 0
        max_square = 0


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        max_square = 0
        cols = [0 for _ in matrix[0]]
        print(cols)
        for row in matrix:
            for i, col in enumerate(row):
                if col == "0":
                    cols[i] = 0
                else:
                    cols[i] += 1
            max_square = self.helper(cols, max_square)
        return max_square * max_square

    def helper(self, cols: List[int], max_square) -> int:
        next_max = max_square + 1

        count = 0

        for c in cols:
            if c >= next_max:
                count += 1
            else:
                count = 0
            if count == next_max:
                return max_square + 1

        return max_square
