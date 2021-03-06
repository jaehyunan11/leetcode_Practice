class Solution:
    def isAlienSorted(self, words, order):
        dict = {}
        # map each char in the alien dictionary to its postion
        for index, char in enumerate(order):
            dict[char] = index
        # compare adjacent words
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i+1]
            # words that are the same can be skipped
            if word1 == word2:
                continue
            # longer words, that start with the adjacent word, should not come first
            if len(word1) > len(word2):
                # startswitch return True if the string starts with the specified value.
                if word1.startswith(word2):
                    return False
            # compare each character, it must be smaller or equal to that of the adjacent word
            for j in range(min(len(word1), len(word2))):
                if dict.get(word1[j]) < dict.get(word2[j]):
                    break
                elif dict.get(word1[j]) == dict.get(word2[j]):
                    continue
                else:
                    return False
            return True


class Solution2:
    def isAlienSorted(self, words, order):
        dict = {}
        for idx, char in enumerate(order):
            dict[char] = idx
        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]
            for k in range(min(len(word1), len(word2))):
                if word1[k] != word2[k]:
                    if dict[word1[k]] > dict[word2[k]]:
                        return False
                    break
        else:
            if len(word1) > len(word2):
                return False
        return True


# class Solution3:
#     def isAlienSorted(self, words, order):
#         dict = {}
#         for idx, char in enumerate(order):
#             dict[char] = idx
#     def isSorted(w1, w2):
#         for c1, c2 in zip(w1, w2):


S = Solution()
S2 = Solution2()
words = ["hello", "leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"
print(S.isAlienSorted(words, order))
print(S2.isAlienSorted(words, order))
