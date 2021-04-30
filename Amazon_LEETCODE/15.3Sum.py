class Solution:
    def threeSum(self, nums):
        # [-1, 0, 1, 2, -1, -4] -> [-4,-1,-1,0,1,2]
        nums = sorted(nums)  # O(nLogn)
        result = set()
        for i in range(len(nums)):
            l = i+1
            r = len(nums) - 1
            # target = 0 - current value
            target = 0 - nums[i]
            while l < r:
                if nums[l] + nums[r] == target:
                    result.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        return list(result)


# TIME : O(N^2) where N is length of numbers and overall O(nlogn+n2) due to sorting the array takes O(nlogn)
# Space : O(N) since we use hashset.
        # res = set()
        # # 1. Split nums into three lists: negative numbers, positive numbers, and zeros
        # n, p, z = [], [], []
        # for num in nums:
        #     if num > 0:
        #         p.append(num)
        #     elif num < 0:
        #         n.append(num)
        #     else:
        #         z.append(num)
        # # 2. Create a separate set for negatives and positives for O(1) look-up times
        # N, P = set(n), set(p)
        # # 3. If there is at least 1 zero in the list, add all cases where -num exists in N and num exists in P
        # #   i.e. (-3, 0, 3) = 0
        # if z:
        #     for num in P:
        #         if -1*num in N:
        #             res.add((-1*num, 0, num))
        # # 4. For all pairs of negative numbers (-3, -1), check to see if their complement (4)
        # #   exists in the positive number set
        # for i in range(len(n)):
        #     for j in range(i+1, len(n)):
        #         target = -1*(n[i]+n[j])
        #         if target in P:
        #             res.add(tuple(sorted([n[i], n[j], target])))
        # # 5. For all pairs of positive numbers (1, 1), check to see if their complement (-2)
        # #   exists in the negative number set
        # for i in range(len(p)):
        #     for j in range(i+1, len(p)):
        #         target = -1*(p[i]+p[j])
        #         if target in N:
        #             res.add(tuple(sorted([p[i], p[j], target])))
        # return res
        # TIME : O(n^2)
S = Solution()
nums = [-1, 0, 1, 2, -1, -4]
print(S.threeSum(nums))
