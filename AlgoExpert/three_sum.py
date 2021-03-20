# O(N^2) TIME since nested for and while loop
# O(n) Space since separate triplets space is used.

class Solution:
    def threeNumberSum(self, array, targetSum):
        # sort array
        array.sort()

        # Create triplets empty array
        triplets = []

        # select initial number
        # create for loop until last 2 numbers in the array.
        for i in range(len(array) - 2):
            # set left and right pointer
            left = i + 1
            right = len(array) - 1
            # loop left < right
            while left < right:
                currentSum = array[i] + array[left] + array[right]
                # currentSum = array[i] + array[left] + array[right]
                if currentSum == targetSum:
                    triplets.append([array[i], array[left], array[right]])
                    left += 1
                    right -= 1
                if currentSum < targetSum:
                    left += 1
                elif currentSum > targetSum:
                    right -= 1
        return triplets


S = Solution()
array = [12, 3, 1, 2, -6, 5, -8, 6]
targetSum = 0
print(S.threeNumberSum(array, targetSum))
# case 1 currentSum == targetSum
# Add to triplets ([array[i], array[left], array[right]])
# move left and right pointers

# if currentSum < targetSum
# increase left pointer to reach out to targetSum

# elif cuurrnetSum > targetSum
# decrease right pointer to reach out to targetSum

# return triplets
