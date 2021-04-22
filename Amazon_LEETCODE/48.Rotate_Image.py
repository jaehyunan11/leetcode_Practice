class Solution:
    def rotate(self, matrix):
        # We can do this in two steps.
        # Reversing the matrix does this:
        # Transposing means: rows become columns, columns become rows.

        matrix.reverse()
        rows = len(matrix)
        for i in range(rows):
            for j in range(i):
                # 3*3 matrix
                # (1,0)->(0,1), (2,0)->(0,2) (2,1) (1,2)
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        return matrix

# TIME: O(M) two step. reversing the each row O(M) because we are moving the value of each cell once. O(M)
# SPACE : O(1) because we do not use any other additional data structures.

# # reverse
# l = 0
# r = len(matrix) - 1
# while l < r:
# 	matrix[l], matrix[r] = matrix[r], matrix[l]
# 	l += 1
# 	r -= 1
# # transpose
# for i in range(len(matrix)):
# 	for j in range(i):
# 		matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
# We want to rotate
# [1, 2, 3],
# [4, 5, 6],
# [7, 8, 9]
# ->
# [7, 4, 1],
# [8, 5, 2],
# [9, 6, 3]]

# We can do this in two steps.
# Reversing the matrix does this:
# [1, 2, 3],
# [4, 5, 6],
# [7, 8, 9]]
# ->
# [7, 8, 9],
# [4, 5, 6],
# [1, 2, 3]

# Transposing means: rows become columns, columns become rows.

# [7, 8, 9],
# [4, 5, 6],
# [1, 2, 3]
# ->
# [7, 4, 1],
# [8, 5, 2],
# [9, 6, 3]


S = Solution()
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(S.rotate(matrix))
