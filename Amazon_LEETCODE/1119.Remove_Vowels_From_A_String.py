class Solution:
    def removeVowels(self, s):
        result = []
        for i in range(len(s)):
            if s[i] not in 'aeiou':
                result.append(s[i])
        return ''.join(result)

# TIME: O(N) N is length of string
# Space: O(N) extra res space need to store N


S = Solution()
s = "leetcodeisacommunityforcoders"
print(S.removeVowels(s))
