from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str):
        ns, np = len(s), len(p)
        if ns < np:
            return []
        p_count = Counter(p)
        s_count = Counter()

        output = []

        # sliding window on the string s
        for i in range(ns):
            # add one more letter
            # on the right side of the window
            s_count[s[i]] += 1
            # remove one letter
            # from the left side of the window
            if i >= np:
                if s_count[s[i-np]] == 1:
                    del s_count[s[i-np]]
                else:
                    s_count[s[i-np]] -= 1
            # compare array in the sliding window
            # with the reference array
            if p_count == s_count:
                output.append(i-np+1)
        return output

# TIME : O(Ns + Np) since it's one pass along both strings.
# SPACE : O(1) because pCount and sCount contain not more than 26 elements


S = Solution()
s = "cbaebabacd"
p = "abc"
print(S.findAnagrams(s, p))
