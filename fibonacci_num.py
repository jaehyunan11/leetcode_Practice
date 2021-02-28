class Solution:
    def fib(self, n):
        if n <= 1:
            return n
        return self.fib(n-1) + self.fib(n-2)


class Solution2:
    def fib(self, n):
        x = 0
        y = 1
        if n == 0:
            return 0
        elif n == 1:
            return y
        for i in range(1, n):
            x, y = y, x+y
            print(f"{i} round ")
            print(f"x:{x}")
            print(f"y:{y}")
            print(f"x+y:{x+y}")
        return y

# Time complexity : O(N)
# Space Complexity : O(n)


s = Solution2()
print(s.fib(5))
