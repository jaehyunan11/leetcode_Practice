class Solution:
    def searchMatrix(self, matrix, target):
        print(len(matrix))
        print(len(matrix[0]))
        for row in matrix:
            if target in row:
                return True
        return False
# Bruce Force
# TIME : O(n*m) since n * m search in the matrix
# Space : O(1)

    def searchMatrix2(self, matrix, target):
        # empty matrix is doesn't contain target
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        # starting point
        row, col = 0, len(matrix[0])-1
        while row < len(matrix) and col >= 0:
            # num in matrix is greater than target then pointer move to bottom
            if matrix[row][col] < target:
                row += 1
            # num in matrix is less than target then pointer move to left
            elif matrix[row][col] > target:
                col -= 1
            else:
                return True
        return False


# TIME O(n+m)
# Space O(1) :
S = Solution()
matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [
    3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]

target = 5
print(S.searchMatrix(matrix, target))
print(S.searchMatrix2(matrix, target))
