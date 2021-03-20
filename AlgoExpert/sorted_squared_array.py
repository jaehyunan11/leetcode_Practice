class Solution:
    def sortedSquaredArray(self, array):
        sortedSquares = [0 for _ in array]
        smallerValueIdx = 0
        largerValueIdx = len(array) - 1

        for idx in reversed(range(len(array))):
            smallerValue = array[smallerValueIdx]
            largerValue = array[largerValueIdx]
            if abs(smallerValue) > abs(largerValue):
                sortedSquares[idx] = smallerValue * smallerValue
                smallerValueIdx += 1
            else:
                sortedSquares[idx] = largerValue * largerValue
                largerValueIdx -= 1
        return sortedSquares


# TIME : O(N)
# Space : O(N) use separate sorted array where n is lenght of the array

    def sortedSquaredArray2(self, array):

        sortedSquares = [0 for _ in array]

        for idx in range(len(array)):
            value = array[idx]
            sortedSquares[idx] = value * value
        sortedSquares.sort()
        return sortedSquares

# TIME : O(nLog(n)) since sort the array which is logn with n length of the array
# Space : O(N) use separate sorted array where n is lenght of the array


S = Solution()
array = [1, 2, 3, 5, 6, 8, 9]
print(S.sortedSquaredArray(array))


S = Solution()
array = [1, 2, 3, 5, 6, 8, 9]
S.sortedSquaredArray(array)
