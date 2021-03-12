"""
Input: str = “abaaa”
Output: 5
Palindromic sub-strings are “a”, “aa”, “aaa”, “aba” and “b”

Input: str = “abcd”
Output: 4
"""

# Is string[i] equal to string[j]
# Is string[i+1:j-1] a palindrome?

# 1. a single character, which is a palindrome by definition
# example: "a"
# 2. two charactesr that are the same
# example: "aa"
# 3. to determine if bigger substring is a palindrome you should know
# if the inner substring is the palindrome and if the outer characters match


class Solution:
    def countSubstring(self, s):
        # edge case s is not available
        if not s:
            return 0

        n = len(s)
        res = 0

        # create a matrix to store info about the substring
        dp = [[0 for i in range(n)] for j in range(n)]

        # set single characters as palindromes
        for i in range(n):
            dp[i][i] = 1
            res += 1
        #
        for col in range(1, n):
            for row in range(col):
                # every two chars are palindromes (two characters are same)
                if row == col - 1 and s[col] == s[row]:
                    dp[row][col] = 1
                    res += 1

                # to determine if substring is a palindrome you should know
                # 1) if thedinner substring is the palindrome and
                # 2) if the outer charactesrs match
                # inner substring == 1 means palindrome and outer col and row is same
                elif dp[row+1][col-1] == 1 and s[col] == s[row]:
                    dp[row][col] = 1
                    res += 1
        print(dp)
        return res

        # TIME Complexity : O(N^2) + O(N) = O(N)
        # Space Complexity : O(N^2) allocate extra space to hold all dp states.

        # fill the matrix
        # example: "aaa"
        #      0  1  2
        #      a  a  a
        # 0 a [1, 1, 1]
        # 1 a [0, 1, 1]
        # 2 a [0, 0, 1]


S = Solution()
s = "aaaaa"
print(S.countSubstring(s))
