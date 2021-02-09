from collections import defaultdict


class Solution:
    def __init__(self, nums):
        self.nums = nums

    def singleNumber(nums):
        hash_table = defaultdict(int)
        for i in nums:
            hash_table[i] += 1
        for i in hash_table:
            if hash_table[i] == 1:
                return i


# class Solution:
#     def __init__(self, nums):
#         self.nums = nums

#     def singleNumber(nums):
#         num = 0
#         for n in nums:
#             num ^= n
#         return num

nums = [2, 2, 1, 4]
s = Solution
print(s.singleNumber(nums))
