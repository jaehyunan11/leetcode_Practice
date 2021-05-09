class Solution:
    def repeatedSubstringPattern(self, s):
        rep = ''
        length_s = len(s)
        # the reason for loop half is it is enough to check.
        # over half -> you can't find repeation e.g. 6 -> 3 + 3 repeation
        for i in range(length_s // 2):
            rep += s[i]
            if length_s % len(rep) == 0:  # e.g. 10 % 3 = 1 never get repeation
                # "ab" * (4 // 2) == "abab" == "abab"
                if rep * (length_s // len(rep)) == s:
                    return True
        return False

# TIME: O(1/2N) -> O(N)
# SPACE: O(N) since we are using rep="" to compare with s.


S = Solution()
s = "abab"
print(S.repeatedSubstringPattern(s))
