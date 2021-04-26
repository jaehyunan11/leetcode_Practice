class Solution:
    def reverseWords(self, s):
        # split into single word
        s = s.split()
        # left, right
        # Loops left < right
        # swap left and right
        # increase left += 1
        # decrese right -= 1
        # return ' '.join(s) # single space join

        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return ' '.join(s)

# TIME : O(N)
# Space : O(1)


S = Solution()
s = "the sky is blue"
print(S.reverseWords(s))
