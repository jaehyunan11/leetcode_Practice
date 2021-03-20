class Solution:
    def twoSum(self, nums, target):
        # index
        dict = {}

        # loop the nums and store pair (target-num) in the dict
        for i in range(len(nums)):
            num = nums[i]
            pair = target - num
            if pair in dict:
                return [dict[pair], i]
            else:
                dict[pair] = i
        print(dict)
        return False

# TIME: O(N) We traver the list of containing n elements
# Space : O(N) the extra space required depends on the number of items stored in the hash table.


S = Solution()
nums = [2, 7, 11, 15]
target = 9
print(S.twoSum(nums, target))
