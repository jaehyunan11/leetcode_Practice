"""
Given a string s, return the first non-repeating character in it and return its index. 
If it does not exist, return -1.
"""
from collections import Counter


class Solution:
    def firstUniqChar(self, s):
        count = Counter(s)
        print(count)

        for idx, chr in enumerate(s):
            if count[chr] == 1:
                return idx
        return -1


# class Solution:
#     def firstUniqChar(self, s):
#         letters = {}
#         res = 0

#         for i, c in enumerate(s):
#             if c in letters:
#                 letters[c] += 1
#             else:
#                 letters[c] = 1

#         # check the unique index
#         for key, value in letters.items():
#             if value == 1:
#                 res = s.index(key)
#                 return res
#         return -1

# TIME : O(N) iterate to find number of char.
# SPACE : O(1)  because English alphabet contains 26 letters.


S = Solution()
s = "loveleetcode"
print(S.firstUniqChar(s))
