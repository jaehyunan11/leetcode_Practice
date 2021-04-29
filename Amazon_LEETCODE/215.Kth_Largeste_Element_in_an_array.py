from heapq import nlargest


class Solution:
    def findKthLargest(self, nums, k):
        # nums.sort()
        # return nums[-k]

        return nlargest(k, nums)[-1]
# TIME : O(NLogK)
# SPACE : O(K)


S = Solution()
nums = [3, 2, 1, 5, 6, 4]
k = 2
print(S.findKthLargest(nums, k))
