"""
01, 10 -- reverse --> 10, 01
01, 10 --padding with zeros--> 001, 010
10, 01 --padding with ones--> 110, 101
001, 010 + 110, 101 --concatenate--> 001, 010, 110, 101

"""


class Solution:
    def grayCode(self, n):
        res = []

        # x << y = x * 2**y
        # 1*2^n
        # 
        for i in range(1 << n):
            # i >> 1 1 spot to the left
            res.append(i ^ (i >> 1))
        return res
# TIME: O(2^n) 2^n iterate
# Space : O(1) constant space store


S = Solution()
n = 2
print(S.grayCode(n))
