from collections import Counter


class Solution:
    def frequencySort(self, s):
        counts = Counter(s)
        print(counts)

        # string builder
        string_builder = []

        for letter, freq in counts.most_common():
            string_builder.append(letter * freq)
            print(string_builder)
        return "".join(string_builder)


S = Solution()
s = "tree"
print(S.frequencySort(s))
