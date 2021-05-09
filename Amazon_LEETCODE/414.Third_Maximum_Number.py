class Solution:
    def thirdMax(self, nums):
        # Set Maximum
        # Loop nums
        # add num to maximum set
        # if maximum set > 3:
        #   remove min num in maximum set
        # if maximum set == 3:
        #   return min(maximum)
        # return max(maximum)

        maximum = set()
        for num in nums:
            maximum.add(num)
            if len(maximum) > 3:
                maximum.remove(min(maximum))
        if len(maximum) == 3:
            return min(maximum)
        return max(maximum)

# TIME: O(N)
# SPACE : O(1)


S = Solution()
nums = [3, 2, 1]
print(S.thirdMax(nums))
