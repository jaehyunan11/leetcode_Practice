class Solution:
    def subarraySum(self, nums, k):
        # start the hashmap with 0 size or
        # we already have a hashmap of size 0, 1time or
        # we already have subarraySum of size 0 , 1time
        sum_dict = {0: 1}
        # sum_dict ={sumarray:count}
        n = len(nums)
        count = 0
        s = 0

        for num in nums:
            s += num  # calculate the cummulative sum
            # if the subarray is found
            if s-k in sum_dict:
                count += sum_dict[s-k]
                # if no subarray is found so keep on updating the hashmap with the frequency
            if s in sum_dict:
                # we already have val in hashmap so update the frequency
                sum_dict[s] += 1
            else:
                sum_dict[s] = 1
        return count
        # Sum_dict {0:1, 1:1, 3:1, 6:1}

# TIME : O(N) The entire numsnums array is traversed only once.
# SPACE : O(N) Hashmap mapmap can contain up to nn distinct entries in the worst case.


S = Solution()
nums = [1, 1, 1]
k = 2
print(S.subarraySum(nums, k))
