class Solution:
    def count(self, s, c):
        # count variable
        res = 0

        for i in range(len(s)):
            # Checking character in string
            if s[i] == c:
                res += 1

        return res

# TIME COMPLEXITY : O(N)
# SPACE COMPLEXITY : O(1)


S = Solution()
str = "geeksforgeeks"
c = "e"
print(S.count(str, c))
