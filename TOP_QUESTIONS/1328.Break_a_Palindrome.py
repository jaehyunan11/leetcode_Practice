class Solution:
    def breakPalindrome(self, palindrome):
        # try to break palindrome by changing other than middle char
        # if change middle char, it is still palindrome

        word = list(palindrome)
        length = len(word) // 2
        for i in range(length):
            if word[i] > 'a':
                word[i] = 'a'
                print(word)
                return ''.join(word)
        if length > 0:
            word[-1] = 'b'
            return ''.join(word)

# Time : O(N/2) -> O(N) where N is length of char of palidrome
# Space : O(N) N is length of storing the words


S = Solution()
palindrome = "abccba"
print(S.breakPalindrome(palindrome))
