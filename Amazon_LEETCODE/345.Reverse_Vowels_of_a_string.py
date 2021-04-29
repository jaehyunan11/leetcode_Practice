class Solution:
    def reverseVowels(self, s):
        # Make s in list eat -> ['e','a', 't']
        # iterate left and right
        # if s[left] and s[right] are in vowels
        # then swap
        # if s[left] not in vowels then left += 1 and continue
        # if s[right] not in vowels then right -= 1 and continue
        # left += 1
        # right -= 1
        # return ''.join(s)
        vowels = set('aeiouAEIOU')
        s = list(s)
        left = 0
        right = len(s) - 1
        while left <= right:
            if s[left] in vowels and s[right] in vowels:
                s[left], s[right] = s[right], s[left]
            elif s[left] not in vowels:
                left += 1
                continue
            elif s[right] not in vowels:
                right -= 1
                continue
            left += 1
            right -= 1
        return ''.join(s)

# TIME : O(N) N is length of string.
# SPACE : O(1) we don't use extra space to store new string


S = Solution()
s = "hello"
print(S.reverseVowels(s))
