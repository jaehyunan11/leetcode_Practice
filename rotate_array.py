# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]

# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation:
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]

# class Solution:
#     def rotate(self, nums, k):
#         n = len(nums)
#         k %= n
#         self.reverse(nums, 0, len(nums) - 1)
#         self.reverse(nums, 0, k-1)
#         self.reverse(nums, k, len(nums)-1)

#     def reverse(self, arr, start, end):
#         while start < end:
#             arr[start], arr[end] = arr[end], arr[start]
#             start += 1
#             end -= 1


# nums = [1, 2, 3, 4, 5, 6, 7]
# k = 3
# s = Solution()
# print(s.rotate(nums, k))

###################################################

# arr = [1, 2, 3, 4, 5]
# k = 2  # k times rotate

# print("Original Array")
# for i in range(0, len(arr)):
#     print(arr[i])

# Roate the given array by k times toward left


def rotate(arr, k):
    for i in range(0, k):
        # store the first element of the array
        first = arr[0]
        for j in range(0, len(arr)-1):
            arr[j] = arr[j+1]
        arr[len(arr)-1] = first
    return arr


arr = [1, 2, 3, 4, 5]
k = 2  # k times rotate
print(rotate(arr, k))

# for i in range(0, k):
#     # store the first element of the array
#     temp = arr[0]
#     for j in range(0, len(arr) - 1):
#         # shift element of array by one
#         arr[j] = arr[j+1]
#     # last element
#     arr[len(arr) - 1] = temp

# print("Array after left rotation: ")
# for i in range(0, len(arr)):
#     print(arr[i]),

#######################################################
