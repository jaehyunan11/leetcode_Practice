class Solution:
    def longestCommonPrefix(self, strs):
        # The * character is known as the unpacking operator
        # So without the *, you're doing zip( [[1,2,3],[4,5,6]] ).
        # With the *, you're doing zip([1,2,3], [4,5,6])
        l = list(zip(*strs))
        prefix = ""
        print(l)
        for i in l:
            print(i)
            # common prefix -> add to prefix
            if len(set(i)) == 1:
                prefix += i[0]
            # not common just break
            else:
                break
        return prefix

# TIME : O(S) where S is the sum of all characters in all strings.
# Space : O(1) We only used constant extra space.


S = Solution()
strs = ["flower", "flow", "flight"]
print(S.longestCommonPrefix(strs))
