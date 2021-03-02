class Solution:
    def topKFrequent(self, words, K):
        # Count the words and store in the dict
        self.dict = {}

        # Case 1
        if words == []:
            return 0
        elif len(words) == 1:
            return works[0]
        else:
            for word in words:
                if word not in self.dict:
                    self.dict[word] = 1
                else:
                    self.dict[word] += 1
        # sorted by value self.dict[x] and second sort reference as key
        topk = sorted(self.dict, key=lambda x: (-self.dict[x], x))
        print(self.dict)
        print(f"TopK: {topk}")
        return topk[:K]


s = Solution()
words = ["i", "love", "leetcode", "i", "love", "coding"]
words2 = ["the", "day", "is", "sunny",
          "the", "the", "the", "sunny", "is", "is"]
K = 2
K2 = 4
print(s.topKFrequent(words, K))
print(s.topKFrequent(words2, K2))
