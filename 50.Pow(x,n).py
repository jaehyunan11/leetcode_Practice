class Solution:
    def myPow(self, x: float, n: int):
        # base case 1
        if n == 0:
            return 1.0
        elif n < 0:
            # e.g. x ^ -3 = (1/x)^3
            return self.myPow(1/x, -n)
        elif n % 2 == 0:
            # e.g. 2^4 = (2*2)^ 4/2
            return self.myPow(x*x, n/2)
        else:
            # e.g. 2^3 = 2 * 2^(3-1)
            return x * self.myPow(x, n-1)


S = Solution()
x = 2.00000
n = 10
print(S.myPow(x, n))
