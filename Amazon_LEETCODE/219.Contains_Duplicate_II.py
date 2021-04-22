class Solution:
    def containsNearbyDuplicate(self, nums, k):
        # Map
        # [1,0,1,1]
        # Map
        """
        1:0 -> 1:2
        0:1
        """
        hash_map = {}
        for i, v in enumerate(nums):
            if v in hash_map and i - hash_map[v] <= k:
                return True
            else:
                # update index for the duplicated value in the map
                hash_map[v] = i
        return False


# TIME : O(N) We iterate length of nums and to find duplicate and compute difference
# SPACE : O(N) We use extra space to store length of nums in hash_map

S = Solution()
nums = [1, 0, 1, 1]
k = 2
print(S.containsNearbyDuplicate(nums, k))
