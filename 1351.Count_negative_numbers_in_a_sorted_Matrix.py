class Solution:
    # def countNegatives(self, grid):
    #     count = 0
    #     for row in grid:
    #         for element in row:
    #             if element < 0:
    #                 count += 1
    #     return count

    # def countNegatives(self, grid):
    #     m, n = len(grid), len(grid[0])
    #     row, col, count = 0, n-1, 0
    #     while row < m and col >= 0:
    #         print(f"row: {row}", f"col: {col}")
    #         if grid[row][col] < 0:
    #             count += m - row
    #             col -= 1
    #         else:
    #             row += 1
    def countNegatives(self, grid):
        row_len = len(grid)
        col_len = len(grid[0])

        row, col, count = 0, col_len - 1, 0

        while row < row_len and col >= 0:
            if grid[row][col] < 0:
                count += row_len - row
                print(count)
                col -= 1
            else:
                row += 1
        return count

# TIME and Space complexity : O(N+M) where length of row + length of col

        # def countNegatives(self, grid):

        #     def bin(row):
        #         start, end = 0, len(row)
        #         while start < end:
        #             mid = start + (end - start) // 2
        #             if row[mid] < 0:
        #                 end = mid
        #             else:
        #                 start = mid+1
        #         return len(row) - start

        #     count = 0
        #     for row in grid:
        #         count += bin(row)
        #     return(count)


S = Solution()
grid = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2]]
print(S.countNegatives(grid))
