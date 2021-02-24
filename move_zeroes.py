class Solution:
    def moveZeroes(self, nums):
        # 1) set position
        pos = 0
        # 2) loop to navigates non zeros
        for i in range(len(nums)):
            el = nums[i]
            # 3) if there is non zero, swap it with the num in the postion.
            if el != 0:
                nums[pos], nums[i] = nums[i], nums[pos]
                pos += 1
        return nums

# class Solution2:
#     def moveZeros(self, nums):
#         pos = 0
#         swap = 0
#         for i in range(len(nums)):
#             el = nums[i]
#             if el != 0:
#                 swap = nums[pos]
#                 nums[pos] = el
#                 el = swap
#                 pos += 1
#         return nums


s = Solution()
nums = [0, 1, 0, 3, 12]
print(s.moveZeroes(nums))
