class Solution:
    def __init__(self, num):
        self.num = num

    def isArmstrong(num):
        # 1) Cast N to a list of each digit. e.g. ["1", "2", "3"]
        num_list = list(str(num))

        # 2) Compute the value we want to compare to N
        armstrong_value = sum([int(i) ** len(num_list) for i in num_list])

        # 3) See if the value is the same
        return armstrong_value == num


s = Solution
num = 153
print(s.isArmstrong(num))
