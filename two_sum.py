# Step 1 : Verify the constraints
# Are there duplicate numbers in the array?
# Are all the numbers positives or negatives?
# Will there always be a solution available?
# What do we return if there's no solution?
# can there by multiple pairs that add up to the target?
# Step 2 : Figure out without code

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
                print(index_map)
        return False


s = Solution
nums = [2, 7, 11, 15]
target = 26

res = s.twoSum(nums, target)
print(res)
