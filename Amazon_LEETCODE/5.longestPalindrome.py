class Solution:
    def longestPalindrome(self, s):
        logestSub = ""
        for i in range(len(s)):
            # odd case like "aba"
            temp = self.helper(s, i, i)
            if len(temp) > len(logestSub):
                logestSub = temp
            # even case like "abba"
            temp = self.helper(s, i, i+1)
            if len(temp) > len(logestSub):
                logestSub = temp
        return logestSub

    def helper(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            # expand left and right
            left -= 1
            right += 1
        return s[left+1:right]

# TIME : O(N^2) Since expanding a palindrome around its center could take O(n) tim
# SPACE : O(1) contant space to store string


S = Solution()
s = "babad"
print(S.longestPalindrome(s))
