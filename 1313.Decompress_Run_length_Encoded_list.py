class Solution:
    def decompressRLElist(self, nums):
        i = 0
        res = []
        while i < len(nums):
            res += ([nums[i+1]] * nums[i])
            i += 2  # two pairs
        return res

# TIME and Space : O(N) where N is length of nums empty res space is required.


obj = Solution()
print(obj.decompressRLElist([1, 2, 3, 4]))
