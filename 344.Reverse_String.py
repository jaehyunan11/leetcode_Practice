class Solution:
    def reverseString(self, s):
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left, right = left+1, right-1
        return s

# Time complexity : O(N) to swap N/2N/2 element.
# Space complexity : O(1), it's a constant space solution.


S = Solution()
s = ["h", "e", "l", "l", "o"]
print(S.reverseString(s))
