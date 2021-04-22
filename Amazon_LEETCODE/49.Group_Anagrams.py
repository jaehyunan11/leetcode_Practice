class Solution:
    def groupAnagrams(self, strs):
        # stored each strs
        # loop the strs
        # If it is existed in dict then add the str from dict[key] to ret.
        # Else add to ret
        # store dict[key] with index, dict[key] = index
        # increase index +1

        ret = []
        dict = {}
        index = 0
        for str in strs:
            # To match the str
            key = ''.join(sorted(str))
            if key in dict:
                ret[dict[key]].append(str)
            else:
                ret.append([str])
                dict[key] = index
                index += 1
        return ret

# TIME : O(NKlog(N)) length of the strengh to iterate and sorted the str
# N: length of strs, K: maximum length of string
# SPACE : O(NK) total information content stored in ans


S = Solution()
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(S.groupAnagrams(strs))
