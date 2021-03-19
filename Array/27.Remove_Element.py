class Solution:
    def removeElement(self, nums, val):
        while val in nums:
            nums.remove(val)
        return len(nums), nums


S = Solution()
nums = [3, 2, 2, 3]
val = 3
print(S.removeElement(nums, val))
