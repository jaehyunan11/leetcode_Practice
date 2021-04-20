class Solution:
    def subsets(self, nums):
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i+1)

            # decision NOT to include nums[i]
            subset.pop()
            dfs(i+1)
        dfs(0)
        return res

    # def subsets(self, nums):
    #     output = [[]]
    #     for num in nums:
    #         output += [curr + [num]for curr in output]
    #     return output
        # output = [[],[1],[2], [1,2], [3], [1,3], [2,3]]
        # []
        # [] + [1] = [1]
        # [] + [2] = [2]
        # [1] + [2] = [1,2]
        # [] + [3] = [3]
        # [1] + [3] = [1,3]
        # [2] + [3] = [2,3]
        # [1,2] + [2] = [1,2,3]

    # TIME : O(N * 2^N) to generate all subset and then copy them into putput list.
    # SPACE : O(N * 2^N) This is exactly the number of solutions for subsets multiplied by the number NN of elements to keep for each subset.


# TIME : n * 2^n
# SPACE
S = Solution()
nums = [1, 2, 3]
print(S.subsets(nums))
