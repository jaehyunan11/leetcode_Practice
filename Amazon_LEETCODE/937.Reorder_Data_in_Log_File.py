class Solution:
    def reorderLogFiles(self, logs):
        # letter logs (all words consist of lower case)
        # digit logs: (All words consist of digit)
        # letter-logs > digit-logs
        # letter-logs are sorted lexicographically
        # digit-logs maintain their relative ordering
        # 1) Create empty array for both digits and letters
        # digits = []
        # letters = []
        # # 2) Loop the logs and update to each digits and letters array based on the condition.
        # for log in logs:
        #     #  3) letter logs comes before digit log
        #     # e.g. ["a1 9 2 3 1"] -> ["a1", "9", "2", "3", "1"]
        #     if log.split()[1].isdigit():
        #         digits.append(log)
        #     else:
        #         letters.append(log)
        # # 4) Try to sort based on first index letter.
        # letters.sort(key=lambda x: x.split()[0])
        # # 5) Try to sort based on last of the index letter
        # letters.sort(key=lambda x: x.split()[1:])

        # return letters + digits

        def sorting_algorithm(log):
            left_side, right_side = log.split(" ", 1)
            print(right_side)

            if right_side[0].isalpha():
                return (0, right_side, left_side)
            else:
                return (1,)

        return sorted(logs, key=sorting_algorithm)


S = Solution()
logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6",
        "let2 own kit dig", "let3 art zero"]
print(S.reorderLogFiles(logs))
