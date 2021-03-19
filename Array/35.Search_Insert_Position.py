# Given a sorted array of distinct integers and a target value, return the index
# if the target is found.
# If not, return the index where it would be if it were inserted in order.


class Solution:
    def searchInsert(self, nums, target):
        left, right = 0, len(nums) - 1
        # create pivot, left, right point
        while left <= right:
            # mid of the arr
            pivot = (left+right) // 2

            # if target is equal to nums[pivot] then return pivot
            if target == nums[pivot]:
                return pivot
            # if target is less than nums[pivot] then move right to pivot-1
            elif target < nums[pivot]:
                right = pivot - 1
            # if target is greater than nums[pivot] then move left to pivot+1
            elif target > nums[pivot]:
                left = pivot + 1
            # if there is no target then return left
        return left

# Time : O(LOG(n))
# Space : O(1)


nums = [1, 3, 5, 6]
target = 5
S = Solution()
print(S.searchInsert(nums, target))
