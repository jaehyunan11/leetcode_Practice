class Solution:
    def reverse(self, x):
        # int -> str -> int (change to str to flip and then change to int)
        # [1:] due to -1 sign
        result = int(str(x)[::-1]) if x >= 0 else -int(str(x)[1:][::-1])

        if -2**31 <= result <= (2**31)-1:
            return result
        else:
            return 0

# TIME: O(Log(n)) flip the str which is Log(N)
# Space : O(1) no extra space is used


S = Solution()
x = 123
print(S.reverse(x))
