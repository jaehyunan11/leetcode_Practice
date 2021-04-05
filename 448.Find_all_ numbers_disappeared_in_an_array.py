class Solution:
    def findDisappearedNumbers(self, nums):
        l = len(nums)
        nums = set(nums)
        ans = []

        for i in range(1, l+1):
            if i not in nums:
                ans.append(i)
        return ans

# TIME and Space complexity are O(N) where N is length of nums.


S = Solution()
nums = [1, 2, 3, 4, 5, 7, 8]
print(S.findDisappearedNumbers(nums))
