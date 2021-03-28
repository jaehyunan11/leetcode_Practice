class Solution:
    def nextGreaterElements(self, nums):
        # bruce force
        # smaller or equal elements can be pushed over top element of stack

        ## LOGIC ##
        # 1. Monotone decreasing stack to find NGE (next greater element)
        # 2. In the first loop, we fill NGE all possible.
        # 3. In the second loop, there might be some elements left in the stack, so we iterate again (without appending to stack) and get NGE
        # 4. The elements that are left in the stack even after second loop are max(nums).

        ## TIME COMPLEXITY : O(N) ##
        ## SPACE COMPLEXITY : O(N) ##

        stack, res = [], [-1] * len(nums)
        # In the first loop, we fill NGE all possible
        for i, num in enumerate(nums):
            while stack and nums[stack[-1]] < num:
                res[stack.pop()] = num
            stack.append(i)
        print(res)
        print(stack)
        for i, num in enumerate(nums):
            while stack and nums[stack[-1]] < num:
                res[stack.pop()] = num
        print(stack)
        return res


S = Solution()
nums = [1, 2, 1]
print(S.nextGreaterElements(nums))
