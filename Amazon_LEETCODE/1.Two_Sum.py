class Solution:
    def twoSumBF(self, nums, target):
        # Check each nums
        # If target - curr == prev: return curr and
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] == target - nums[i]:
                    return i, j
# TIME: O(N^2) we looping through the rest of array which takes O(n) so O(N^2)
# SPACE : O(1)

    def twoSumHash(self, nums, target):
        # Store in hash {num:index}
        # Pair = target - num
        # If pair in hash then return index of the pair and curr idx
        index_map = {}

        for i in range(len(nums)):
            num = nums[i]
            pair = target - num
            if pair in index_map:
                return [index_map[pair], i]
            else:
                index_map[num] = i
        return False

# TIME : O(N) We traverse the list containing n elements once
# SPACE : O(N) extra space required depends on the number of items stored in the hash table


S = Solution()
nums = [2, 7, 11, 15]
target = 9
print(S.twoSumBF(nums, target))
print(S.twoSumHash(nums, target))
