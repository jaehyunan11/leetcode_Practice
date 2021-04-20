class Solution:
    def productExceptSelf(self, nums):
        # [1,2,3,4]
        # scan from left to right [1,1,2,6]
        # scan from right to left [24,12,4,1]
        # multiply 1st and 2nd

        res = [1] * len(nums)  # [1,1,1,1]
        # scan from left to right
        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i-1]
        print(res)
        # scan from right to left
        temp = 1
        for i in range(len(nums) - 2, -1, -1):
            temp = temp * nums[i+1]
            print(temp)
            res[i] = res[i] * temp
        return res
# TIME : O(N) N represents the number of elements in the input array
# Space : O(1) we don't use additioal array for computation.


S = Solution()
nums = [1, 2, 3, 4]
print(S.productExceptSelf(nums))
