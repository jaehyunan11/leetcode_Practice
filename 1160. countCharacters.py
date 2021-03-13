"""
Input: words = ["cat","bt","hat","tree"], 
chars = "atach"
Output: 6
Explanation: 
The strings that can be formed are "cat" and "hat" 
so the answer is 3 + 3 = 6.
"""

from collections import Counter


class Solution:
    def countCharacters(self, words, chars):
        d = {}
        result = 0

        for i in chars:
            d[i] = chars.count(i)
        print(d)

        for word in words:
            result += len(word)
            for char in word:
                if char not in d or d[char] < word.count(char):
                    result -= len(word)
                    break
        return result


# TIME Complexity : O(N^2)
# Space Complexity : O(1)

# class Solution:
#     def countCharacters(self, words, chars):
#         total_chars = Counter(chars)
#         result = 0

#         for word in words:  # O(N)
#             for key, item in Counter(word).items():  # O(N)
#                 print(Counter(word))
#                 if key not in total_chars or item > total_chars[key]:
#                     break
#             else:
#                 result += len(word)
#         return result

# TIME Complexity : O(N^2)

S = Solution()
words = ["cat", "bt", "hat", "tree"]
chars = "atach"
print(S.countCharacters(words, chars))
