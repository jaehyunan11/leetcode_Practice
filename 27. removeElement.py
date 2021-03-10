class Solution:
    def removeElement(self, nums, val):
        while val in nums:
            nums.remove(val)
        return len(nums)

# Time Complexty : O(N)
# Space Complexity : O(1)


S = Solution()
nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
print(S.removeElement(nums, val))
