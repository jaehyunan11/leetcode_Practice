# Input: numbers = [2,7,11,15], target = 9
#Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.

class Solution:
    def twoSum(self, numbers, target):
        index_map = {}

        for i in range(len(numbers)):
            num = numbers[i]
            pair = target - num
            if pair in index_map:
                return [index_map[pair]+1, i+1]
            else:
                index_map[num] = i
        return False

# TIME: O(N) We traverse the list containing n elements once
# SPACE : O(N) extra space required depends on the number of items stored in the hash table


S = Solution()
numbers = [2, 7, 11, 15]
target = 9
print(S.twoSum(numbers, target))
