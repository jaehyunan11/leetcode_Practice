from collections import defaultdict, Counter


class Solution:
    # DefaultDict
    def singleNumber(self, nums):
        hash_table = defaultdict(int)

        for i in nums:
            hash_table[i] += 1
        print(hash_table)
        for i in hash_table:
            if hash_table[i] == 1:
                return i
    # TIME : O(N) where N is nums and O(1) is num in hash table
    # Space : O(N) extra space for hash)table is equal to the number of elements in nums

    # Counter
    def singleNumber_Counter(self, nums):
        c = Counter(nums)
        print(c)

        for key in c.elements():
            if c[key] == 1:
                return key


S = Solution()
nums = [2, 2, 1]
print(S.singleNumber(nums))
print(S.singleNumber_Counter(nums))
