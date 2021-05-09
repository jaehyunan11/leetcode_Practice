from collections import Counter


class Solution:
    def frequencySort(self, s):
        counts = Counter(s)
        print(counts)

        # build up the string builder
        string_builder = []

        for letter, freq in counts.most_common():
            print(counts.most_common())
            string_builder.append(letter*freq)  # e.g. "a" * 4 = "aaaa"
        return "".join(string_builder)

# TIME Complexity : O(nLog(n)) since each of character has to be put in the hashmap and sorted in the Counter
# Space : O(K) which is required to store in hashmap


S = Solution()
s = "tree"
print(S.frequencySort(s))
