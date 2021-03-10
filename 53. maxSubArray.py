class Solution:
    def maxSubArray(self, nums):
        # set curr sum and max sum
        curr_sum = max_sum = nums[0]

        # loop from index 1 to length of nums
        for i in range(1, len(nums)):  # O(N)
            # compare curr_sum
            curr_sum = max(nums[i], curr_sum + nums[i])
            max_sum = max(curr_sum, max_sum)
        return max_sum

        # for i in nums[1:]:  # O(N)
        #     curr_sum = max(i, curr_sum+i)
        #     max_sum = max(curr_sum, max_sum)
        # return max_sum


S = Solution()
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(S.maxSubArray(nums))
