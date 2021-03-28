class Solution:
    def nextGreaterElement(self, nums1, nums2):
        # stack = []
        # diff = {}

        # for pos, val in enumerate(nums2):
        #     while stack and stack[-1] < val:
        #         diff[stack.pop()] = val
        #     stack.append(val)
        # print(stack)
        # print(diff)
        # for pos in range(len(nums1)):
        #     if nums1[pos] in diff:
        #         nums1[pos] = diff[nums1[pos]]
        #     else:
        #         nums1[pos] = -1
        # return nums1


S = Solution()
nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]

print(S.nextGreaterElement(nums1, nums2))
