class Solution:
    def merge(self, nums1, m, nums2, n):
        # Pointer m-1,n-1 (nums1, nums2 pointers)
        # Pointer m+n-1 (nums1's last pointer)
        # compare m-1, n-1 pointers
        # if nums1[m-1] > nums2[n-1]:
        # nums1[m+n-1] = nums1[m-1]
        # decrement m -= 1 pointer
        # if nums1[m-1] < nums2[n-1]:
        # nums1[m+n-1] = nums2[n-1]
        # decrement n -= 1 pointer
        # Edge case only 1 of each nums1,2 are existed.
        # copy nums1[:n] = nums2[:n]

        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        # still n > 0 then copy n to nums1
        nums1[:n] = nums2[:n]
        return nums1


S = Solution()
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
print(S.merge(nums1, m, nums2, n))
