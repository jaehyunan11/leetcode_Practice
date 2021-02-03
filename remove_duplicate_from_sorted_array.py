# Input: nums = [1,1,2]
# Output: 2, nums = [1,2]
# Explanation: Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the returned length.

class Solution:
    def removeDuplicates(self, nums):
        i = 0
        if len(nums) == 0:
            return 0
        # Time Complexity = O(N), Space Complexity = O(1)
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                nums[i+1] = nums[j]
                i += 1
        return i + 1


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
s = Solution()
print(s.removeDuplicates(nums))
