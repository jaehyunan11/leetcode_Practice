class Solution:
    def twoSum(self, nums, target):
        # index_map to store pair of different between target and num
        index_map = {}

        for i in range(len(nums)):
            num = nums[i]
            pair = target - num
            print(index_map)
            if pair in index_map:
                return [index_map[pair], i]
            else:
                index_map[num] = i
        return False

    def twoSum2(self, nums, target):
        h = {}

        for i, num in enumerate(nums):
            n = target - num
            print(list(enumerate(nums)))
            print(h)
            if n not in h:
                h[num] = i
            else:
                return [h[n], i]

# Time : O(n) we traverse the list containing n elements
# Space : O(n) since the extra space required depends on the number of items store in the hash


S = Solution()
nums = [3, 2, 4]
target = 6
print(S.twoSum(nums, target))
print(S.twoSum2(nums, target))
