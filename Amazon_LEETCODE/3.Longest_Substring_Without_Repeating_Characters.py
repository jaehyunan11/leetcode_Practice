class Solution:
    def lengthOfLongestSubstring(self, s):
        # set seen : collection of characters
        # set left, right pointer to navigate string
        # set max_len = 0
        seen = set()
        left, right, max_len = 0, 0, 0
        while right < len(s):
            curr_str = s[right]
            # there is no duplicate case
            if curr_str not in seen:
                seen.add(curr_str)
                max_len = max(max_len, len(seen))
                right += 1
            # there is duplicate case
            else:
                seen.remove(s[left])
                left += 1
        return max_len

# TIME : O(N)
# SPACE : O(min(m,n))
# n : The size of the set is upper bounded by the size of the string n
# m : the size of the charset m


S = Solution()
s = "abcabcbb"
print(S.lengthOfLongestSubstring(s))
