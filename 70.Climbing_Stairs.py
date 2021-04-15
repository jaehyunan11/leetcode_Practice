class Solution:
    def climbStairs(self, n):
        # base case
        if n == 1:
            return 1
        first = 1
        second = 2

        for i in range(3, n+1):
            third = first + second
            first = second
            second = third
        return second

# TIME : O(n) single loop n is quired to calculate nth fibonacci number
# SPACE : O(1) constant space use


S = Solution()
n = 5
print(S.climbStairs(n))
