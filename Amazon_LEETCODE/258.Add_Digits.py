class Solution:
    def addDigtis(self, nums):
        # Divisible by 9 if and only if sum of its digits is divisible by 9
        """
        divisible by 9 (solo digit)
        10 -> 1
        11 -> 2
        12 -> 3

        20 -> 2
        21 -> 3

        28 -> 10 -> 1
        """
        if nums == 0:
            return 0
        if nums % 9 == 0:
            return 9
        else:
            return nums % 9

# TIME : O(1)
# Space : O(1)


S = Solution()
nums = 38
print(S.addDigtis(nums))
