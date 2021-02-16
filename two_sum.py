class Solution:
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target

    def twoSum(nums, target):
        index_map = {}

        for i in range(len(nums)):
            num = nums[i]
            pair = target - num
            if pair in index_map:
                return [index_map[pair], i]
            else:
                index_map[num] = i
        return False


s = Solution
nums = [2, 7, 11, 15]
target = 9

res = s.twoSum(nums, target)
print(res)
