class Solution:
    def maxSubArray(self, nums):
        # Define curr_Sum and max_sum
        # loop through nums and compare the curr_Sum and max_sum to find out final_max_sum
        # return max_sum

        # Set first index of nums is curr_sum and max_sum
        curr_sum = max_sum = nums[0]

        # Iterate nums from second index

        for i, num in enumerate(nums[1:]):
            curr_sum = max(num, curr_sum+num)
            max_sum = max(curr_sum, max_sum)
        return max_sum

# TIME : O(N) Iterate nums and compute and compare curr_sum vs max_sum
# SPACE : O(1) We are not creating extra space to store max_sum


S = Solution()
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(S.maxSubArray(nums))
