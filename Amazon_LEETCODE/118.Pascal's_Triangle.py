class Solution:
    def generate(self, numsRows):
        """
            1
           1 1
          1 2 1
         1 3 3 1
        1 4 6 4 1
        """
        """
		c[i][j] = c[i-1][j-1] + c[i-1][j]
		1
		1 1
		1 2 1
		1 3 3 1
		1 4 6 4 1
        """

        # DP way
        triangle = []

        # Find number of row
        for row_num in range(numRows):
            row = [1] * (row_num+1)
            # Each triangle element is equal to the sum of the elements
            # above-and-to-the-left and above-and-to-the-right
            # we only see based on the length of the row
            for j in range(1, len(row)-1):
                row[j] = triangle[row_num-1][j-1] + triangle[row_num-1][j]
            triangle.append(row)
            print(triangle)
        return triangle

# TIME : O(numRows^2) O(N^2) since we iterate numRows
# SPACE : O(nums) Because we need to store each number that we update in triangle,
#                the space requirement is the same as the time complexity.


S = Solution()
numRows = 5
print(S.generate(numRows))
