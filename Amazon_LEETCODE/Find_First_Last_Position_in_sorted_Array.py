"""

Input : arr[] = {1, 3, 5, 5, 5, 5, 67, 123, 125}    
        x = 5
Output : First Occurrence = 2
         Last Occurrence = 5


Input : arr[] = {1, 3, 5, 5, 5, 5, 7, 123, 125 }    
        x = 7
Output : First Occurrence = 6
         Last Occurrence = 6

"""


class Solution:
    def first(self, arr, x):

        low = 0
        high = len(arr) - 1
        res = -1

        while low <= high:
            # binary search logic
            mid = (low + high) // 2

            if arr[mid] > x:
                high = mid - 1
            elif arr[mid] < x:
                low = mid + 1
            # if arr[mid] is same as x
            # we update res and move to the left half
            else:
                res = mid
                high = mid - 1
        return res

    def last(self, arr, x):
        low = 0
        high = len(arr) - 1
        res = -1

        while low <= high:
            # binary search logic
            mid = (low + high) // 2

            if arr[mid] > x:
                high = mid - 1
            elif arr[mid] < x:
                low = mid + 1
            # if arr[mid] is same as x
            # we update res and move to the right half
            else:
                res = mid
                low = mid + 1
        return res
# Time Complexity : O(log n) 
# Auxiliary Space : O(1) 


S = Solution()
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
x = 8
print(S.first(arr, x))
print(S.last(arr, x))
