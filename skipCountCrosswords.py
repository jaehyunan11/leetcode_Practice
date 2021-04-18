class Solution:
    def skipCountCrosswords(self, puzzle):
        row = len(puzzle)
        col = len(puzzle[0])

    def isRowValid(self, row):
        for j in range(1, len(row)):
            if row[j] - row[j-1] != patter_row:
                return False
        return True

    def isColValid(self, col):
        for k in range(1, len(col)):
            if col[k] - col[k-1] != pattern_col:
                return False
        return True


S = Solution()
const_basicSolved = [
    [23, 28, 33],
    [19, 18, 17],
    [15, 8, 1]
]
print(S.skipCountCrosswords(const_basicSolved))
