class Solution:
    def runningSum(self, nums):
        # edge case nums == []
        # return 0

        # for i in range(len(nums)):
            # sum curr += prev
        # return nums

        if len(nums) == 0:
            return 0
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        return nums
# TIME : O(N) n is length of array
# Space : O(1) we don't use any additional space to find the sum

S = Solution()
nums = [1,2,3,4]
print(S.runningSum(nums))