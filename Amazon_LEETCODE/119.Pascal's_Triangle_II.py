class Solution:
    def getRow(self, rowIndex):
        triangle = []

        # find number of row
        for row_num in range(rowIndex+1):
            row = [1] * (row_num+1)
            for j in range(1, len(row)-1):
                row[j] = triangle[row_num-1][j-1] + triangle[row_num-1][j]
            triangle.append(row)
        return triangle[rowIndex]

# TIME : O(Numsrow^2) since we iterate and generate each row and iterate to updat row[j].
# SPACE : O(N) Because we need to store each number that we update in triangle,
#                the space requirement is the same as the time complexity.


S = Solution()
rowIndex = 3
print(S.getRow(rowIndex))
