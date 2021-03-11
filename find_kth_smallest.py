class Solution:
    def kthSmallest(self, arr, k):
        """
         0 1 2 3  4
        [3,5,7,12,19]
        """
        # sort given array
        arr.sort()
        # return k'th element in the sorted array
        return arr[k-1]

    def kthLargest(self, arr, k):
        arr.sort()
        return arr[-k]


s = Solution()
arr = [12, 3, 5, 7, 19]
k = 2
print(s.kthSmallest(arr, k))
print(s.kthLargest(arr, k))
