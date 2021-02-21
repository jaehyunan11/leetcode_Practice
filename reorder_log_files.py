# Case 1 : 2 letter logs
# -> Log#1 (Let3 art zero) vs Log#2 (let2 own kit dog)
# ->-> Let3(Id)/Let2(Id), Ignore the id and compare the second index in alphabatical order
# -> Log#1 (Let3 leet code) vs Log#2 (let2 leet code)
# ->-> If index from second is same then compare the Id (Log#2 Log#3)

# Case 2 : 1 letter log + 1 digit log
# -> Log#1 (Let3 leet code) vs Log#2 (let2 4 3 1 9)
# ->-> Lettter log come before digit log.(Log#1 Log#2)

# Case 3 : 2 digit logs
# -> Log#1 (let3 8 3 5) vs Log#2 (let2 4 3 1)
# ->-> compare with the original index position (Log#2 Log#1) * Log#2 is ahead of Log#1

class Solution:
    def reorderLogFiles(self, logs):
        digits = []
        letters = []

        for log in logs:
            # Letter-logs come before all digit-logs
            # If second log in the array is digit, insert to digits. If not, insert it to letters.
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)
        print(f"Letters: {letters}")
        print(f"Digits: {digits}")
        # sort first letter which is a id in letters
        letters.sort(key=lambda x: x.split()[0])
        print(f"Letters: {letters}")
        # Then sort last of the letters.
        letters.sort(key=lambda x: x.split()[1:])
        print(f"Letters: {letters}")

        # Letter has to come before digits
        return letters + digits


s = Solution()
logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6",
        "let2 own kit dig", "let3 art zero"]
print(s.reorderLogFiles(logs))
