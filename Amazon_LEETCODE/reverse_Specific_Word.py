class Solution:
    def reverse(self, sentence, reverse_word):
        sentence = sentence.split()
        print(sentence)
        for i, w in enumerate(sentence):
            print(i, w)
            if w == reverse_word:
                sentence[i] = sentence[i][::-1]
        return " ".join(sentence)

# TIME : O(N)
# SPACE : O(1)
        #     if w == reverse_word:
        #         reverse_word = reverse_word[::-1]
        #         sentence = sentence[:i] + reverse_word
        #     else:
        #         continue
        # return " ".join(sentence)

        # i = sentence.find(reverse_word)
        # print(i)
        # k = i + len(reverse_word)
        # print(k)
        # reverse_sentence = sentence[:i] + reverse_word[::-1] + sentence[k:]
        # return reverse_sentence


S = Solution()
sentence = "I am working for Amazon"
reverse_word = "Amazon"
print(S.reverse(sentence, reverse_word))
