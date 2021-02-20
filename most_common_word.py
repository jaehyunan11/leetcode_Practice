import re


class Solution:
    def __init__(self, paragraph, banned):
        self.paragraph = paragraph
        self.banned = banned

    def mostCommonWord(paragraph, banned):
        # 1) Create tracking empty dict
        tracking_dict = {}
        print(f"Initial Paragraph: {paragraph}")

        # 2) Replace punctuation by Whitespace (re.sub(pattern, what to replace, string to be applied))
        no_punc_paragraph = re.sub('[^A-Za-z0-9]+', ' ', paragraph)
        print(f"Removed punctuation: {no_punc_paragraph}")

        # 3) Repalce to all lower case
        all_lower = no_punc_paragraph.lower()
        print(f"all_lower case: {all_lower}")

        # 4) Word to split in the list
        words = all_lower.split(' ')
        print(f"words: {words}")

        # 5) Loop through the words and count them.
        for val in words:
            # word in not in banned and not in empty case
            if val not in banned and val != '':
                if val not in tracking_dict:
                    tracking_dict[val] = 1
                else:
                    tracking_dict[val] += 1
        print(f"Tracking dictionary:{tracking_dict}")

        # 6) sorted tracking_dict by descending order
        sorted_dict = sorted(tracking_dict.items(),
                             key=lambda x: (-x[1], x[0]))
        print(f"Sorted Dictionary: {sorted_dict}")

        # 7) return first key in the first index from sorted dictionary
        return sorted_dict[0][0]


paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
s = Solution
print(s.mostCommonWord(paragraph, banned))
