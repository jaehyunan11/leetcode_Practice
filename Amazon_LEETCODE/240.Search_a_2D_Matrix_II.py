class Solution:
    def searchMatrix(self, matrix, target):
        # edge case
        # length of row, col are 0 then return False
        # Start pointer top right corner
        # compare num and target
        # if num > target
        # move row to the left -1
        # elif num < target
        # move col to the bottom +1

        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        row, col = 0, len(matrix[0]) - 1
        while row < len(matrix) and col >= 0:
            if matrix[row][col] < target:
                row += 1
            elif matrix[row][col] > target:
                col -= 1
            else:
                return True
        return False
# TIME : O(n+m) row is decremented m times and col is incremented by n times
# Space : O(1) since it would manipulates a few pointer. its memory foot print is constant.


S = Solution()
matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [
    3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
target = 5
print(S.searchMatrix(matrix, target))
