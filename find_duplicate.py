class Solution:
    def findDuplicate(self, nums):
        # edge case
        if nums == [] or len(nums) == 0:
            return 0
        # Create empty numSet
        numSet = set()
        # loop for each nums in the list
        for num in nums:
            if num not in numSet:
                numSet.add(num)
            else:
                return num


# Time Complexity : O(N)
# Space Complexity : O(1)


class Solution2:
    def findDuplicate(self, nums):
        # edge case#1 (if there is only one num in the list)
        if len(nums) == 1:
            return nums[0]
        # Create empty dict
        dict = {}
        # Loop in Nums list
        for i in nums:
            # add 1 in the dict if num is existed in the dict
            if i in dict:
                dict[i] += 1
            # if not then only add 1 for the number.
            else:
                dict[i] = 1
        # return max duplicate number in the dict
        return max(dict, key=dict.get)


# Time Complexity : O(N)
# Space Complexity : O(1)

s = Solution2()
nums = [1, 3, 4, 2, 2]
print(s.findDuplicate(nums))
