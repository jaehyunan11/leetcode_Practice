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


S = Solution()
m = 3
n = 4
print(S.uniquePaths(m, n))
