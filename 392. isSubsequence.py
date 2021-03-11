class Solution:
    def isSubsequence(self, s, t):
        # set i, j as s, t pointer
        i, j = 0, 0
        # Loop s and t and compare each str in s,t
        # if str in s is same as str in t, increase s pointer.
        while i < len(s) and j < len(j):
            # str in s is subsequence of t
            if s[i] == t[j]:
                i += 1
            j += 1
        if i == len(s):
            return True
        else:
            return False


S = Solution()
s = "abc"
t = "ahbgdc"
print(S.isSubsequence(s, t))


class Solution:
    def isSubsequence(self, s: str, t: str):
        # Main list is not available. True
        if len(s) == 0:
            return True
        # Subsequence list is not available. False
        if len(t) == 0:
            return False
        # i as s pointer, j as t pointer
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        if i == len(s):
            return True
        else:
            return False


S = Solution()
s = "abc"
t = "ahbgdc"
print(S.isSubsequence(s, t))
