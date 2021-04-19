
# Given two arrays A and B of positive integers of the same size N.
# The task is to find the maximum sum of products of their elements.
# Each element in A has to be multiplied with exactly one element
# in B or vice versa such that each element of both the arrays appears exactly
# once and the sum of the product obtained is maximum.

# Input : A[] = {1, 2, 3}
# B[] = {4, 5, 1}
# Output : 24
# Explanation : Maximum sum of product is obtained by 5*3+4*2+1*1 = 24.
# Input : A[] = {5, 1, 3, 4, 2}
# B[] = {8, 10, 9, 7, 6}
# Output : 130
# Explanation : Maximum sum of product is obtained by 10*5+9*4+8*3+7*2+6*1 = 130.


# Sort both the arrays.
# Traverse the arrays, and calculate the sum of products of array elements that are at the same index.

class Solution:
    def maximumOfProducts(self, a, b):
        total_sum = 0
        n = len(a)

        a.sort()
        b.sort()

        for i in range(n):
            total_sum += a[i] * b[i]
        return total_sum

# TIME : nLog(N) since we have sorted of a,b as iternate to compute a and b
# SPACE : nLog(N)


S = Solution()
a = [1, 2, 3]
b = [4, 5, 1]
print(S.maximumOfProducts(a, b))
