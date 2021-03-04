class Solution:
    def longestPalindrome(self, s):
        # In case s char is 1
        if len(s) < 2:
            return s
        # result
        res = ""
        # longest length
        resLen = 0

        for idx in range(len(s)):
            # odd length.
            # Check for odd length palindrome with idx at its center
            l = r = idx
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > resLen:
                    res = s[l:r+1]
                    resLen = r-l+1
                l -= 1
                r += 1

            # Check for even length palindrome with idx and idx+1 as its center
            l, r = idx, idx+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > resLen:
                    res = s[l:r+1]
                    resLen = r-l+1
                l -= 1
                r += 1
        return res

# Time complexity : O(N^2)
# Space complexity : O(1)


S = Solution()
string = "babad"
string2 = "cbbd"
print(S.longestPalindrome(string))
print(S.longestPalindrome(string2))
