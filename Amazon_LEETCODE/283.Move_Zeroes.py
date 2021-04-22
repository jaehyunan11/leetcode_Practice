class Solution:
    def moveZeros(self, nums):
        # pointer
        # Iterate nums
        # if we find non-zeros then swipe the nums with the pointer then increase pointer to next
        pos = 0
        for i in range(len(nums)):
            el = nums[i]
            if el != 0:
                nums[pos], nums[i] = nums[i], nums[pos]
                pos += 1
        return nums


S = Solution()
nums = [0, 1, 0, 3, 12]
print(S.moveZeros(nums))
