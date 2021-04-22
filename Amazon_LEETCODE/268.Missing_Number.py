class Solution:
    def missingNumber(self, nums):
        # compare expected sum of nums vs actual sum of nums
        # expected sum of nums len(nums) * len(nums) + 1 // 2
        # return diffrenece of expected sum and actual sum
        expected_sum = len(nums) * (len(nums) + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum

    # TIME : O(N) Suming nums takes O(n)
    # SPACE : O(1)


S = Solution()
nums = [3, 0, 1]
print(S.missingNumber(nums))
