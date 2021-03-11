# memorization
# time complexity : O(2N) => O(N)
# space complexity : O(N)
# def fib(n):
#     memo = {}
#     if n in memo:
#         return memo[n]
#     if n <= 2:
#         return 1
#     memo[n] = fib(n-1) + fib(n-2)
#     print(memo)
#     return memo[n]


# print(fib(6))


def gridTraveler(m, n):
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    return gridTraveler(m-1, n) + gridTraveler(m, n-1)


# def gridTraveler2(m, n):
#     memo = {}
#     key = str(m) + ',' + str(n)
#     if key in memo:
#         return memo[key]
#     if m == 1 and n == 1:
#         return 1
#     if m == 0 or n == 0:
#         return 0
#     memo[key] = gridTraveler(m-1, n) + gridTraveler(m, n-1)
#     print(key)
#     return memo[key]


# print(gridTraveler2(2, 3))
# print(gridTraveler2(18, 18))

class Solution:
    def __init__(self):
        self.dp = {}

    def uniquePaths(self, m, n):
        if (m, n) in self.dp:
            return self.dp[(m, n)]
        if m == 1 and n == 1:
            return 1
        if m == 0 or n == 0:
            return 0
        # path go right or down. (right n -> n-1) (down m -> m-1)
        ans = self.uniquePaths(m, n-1) + self.uniquePaths(m-1, n)
        self.dp[(m, n)] = ans

        print(self.dp)
        return ans

# TIME COMPLEXITY : O(N)
# SPACE COMPLEXITY : O(N)


S = Solution()
m = 2
n = 3
print(S.uniquePaths(m, n))
