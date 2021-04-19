class Solution:
    def numberOfSteps(self, num):
        count = 0
        while num != 0:
            if num % 2 == 0:
                num // 2
            elif num % 2 != 0:
                num -= 1
            count += 1
        return count

# TIME : O(log(N)) When something is halved at every step, it has a O(logn) time complexity.
# Space : O(1) We only use a constant number of integer variables, and so the space complexity is O(1)


S = Solution()
num = 14
print(S.numberOfSteps(num))
