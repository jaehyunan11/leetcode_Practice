class Solution:
    def reverseWords(self, s):
        # reverse entire string first
        # reverse individual word
        # if observe " " space, reverse until space
        # if observe last word
        # reverse
        # return s

        s.reverse()  # O(N)
        print(s)
        idx = 0

        for i in range(len(s)):  # O(N)
            # reverse if meet space
            if s[i] == " ":
                s[idx:i] = s[idx:i][::-1]
                idx = i + 1
            # last word reverse
            if i == len(s) - 1:
                s[idx:] = s[idx:][::-1]
        return s


# TIME : O(N) we are reverse and iterating string which is 2O(N)-> O(N)
# SPACE : O(1) constant space solution

S = Solution()
s = ["t", "h", "e", " ", "s", "k", "y", " ", "i", "s", " ", "b", "l", "u", "e"]
print(S.reverseWords(s))
