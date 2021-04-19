import re
from collections import Counter


class Solution:
    def mostCommonWord(self, paragraph, banned):
        # Convert banned to set for O(1) lookup
        banned = set(banned)
        print(banned)

        # Convert paragraph to lowercase to remove case-sensetivity
        para = paragraph.lower()
        print(para)

        # Extract words from paragraph (remove punctuations from string and extract words)
        para = re.findall("[a-z]+", para)
        print(para)

        # Remove banned words from paragraph
        para = [ele for ele in para if ele not in banned]
        print(para)

        # Compute word frequencies and return most common word.
        return Counter(para).most_common()[0][0]
# TIME : O(N)
# Space : O(N)

        # return Counter([ele for ele in re.findall("[a-z]+",paragraph.lower()) if ele not in banned]).most_common()[0][0]

        # 1)Create Tracking dict
        # 2)Find punctuation and replace with whitespace
        # 3)Make the latest paragraph to all lower case
        # 4)Split the words
        # 5) Count the words if the word is neither empty nor in banned list
        # tracking_dict = {}
        # no_punc_paragraph = re.sub('[^A-Za-z0-9]+', ' ', paragraph)
        # print(no_punc_paragraph)
        # all_low = no_punc_paragraph.lower()
        # words = all_low.split(' ')
        # print(words)
        # for val in words:
        #     if val not in banned and val != '':
        #         if val not in tracking_dict:
        #             tracking_dict[val] = 1
        #         else:
        #             tracking_dict[val] += 1
        # # sorted by number of val and alphabetical order for second sort
        # sorted_dict = sorted(tracking_dict.items(),
        #                      key=lambda x: (-x[1], x[0]))
        # print(sorted_dict)
        # return sorted_dict[0][0]
S = Solution()
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
print(S.mostCommonWord(paragraph, banned))
