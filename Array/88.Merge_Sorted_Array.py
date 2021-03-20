class Solution:
    def merge(self, nums1, m, nums2, n):
        print(nums1)
        print(nums1[:])
        print(nums1[:m])
        print(nums2[:n])
        print(nums1[:m]+nums2[:n])
        print(sorted(nums1[:m]+nums2[:n]))
        nums1[:] = sorted(nums1[:m] + nums2[:n])
        return(nums1)

    def merge1(self, nums1, m, nums2, n):
        if n != 0:
            j = 0
            for i in range(m, len(nums1)):
                nums1[i] = nums2[j]
                j += 1
            nums1 = nums1.sort()
            return nums1


S = Solution()
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
print(S.merge(nums1, m, nums2, n))
