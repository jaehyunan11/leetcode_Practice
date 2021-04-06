class Solution:
    def reverseWords(self, s):
        # Split the str
        s = s.split()
        print(s)
        # Loop the words
        for word in range(len(s)):
            s[word] = s[word][::-1]
        print(s)
        return ' '.join(s)


S = Solution()
s = "God Ding"
print(S.reverseWords(s))
