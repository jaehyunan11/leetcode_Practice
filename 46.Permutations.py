# https://leetcode.com/problems/permutations/discuss/993970/Python-4-Approaches-%3A-Visuals-%2B-Time-Complexity-Analysis
class Solution:
    # Stack
    def stack_permute(self, nums):
        stack = [(nums, [])]  # nums, path
        res = []
        while stack:
            nums, path = stack.pop()
            if not nums:
                res.append(path)
            for i in range(len(nums)):
                newNums = nums[:i] + nums[i+1:]
                stack.append((newNums, path+[nums[i]]))
        return res
    # queue

    def queue_permute(self, nums):
        from collections import deque
        q = deque()
        q.append((nums, []))  # nums, path
        res = []
        while q:
            nums, path = q.popleft()
            if not nums:
                res.append(path)
            for i in range(len(nums)):
                newNums = nums[:i] + nums[i+1:]
                q.append((newNums, path+[nums[i]]))
        return res


S = Solution()
nums = [1, 2, 3]
print(S.stack_permute(nums))
print(S.queue_permute(nums))
