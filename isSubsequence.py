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
