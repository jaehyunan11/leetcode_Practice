class Solution:
    def cominationSum(self, candidates, target):
        candidates.sort()
        ans = []

        def helper(candidates, target, t):
            if not target:
                ans.append(t)
                return
            for i, num in enumerate(candidates):
                if target >= num:
                    helper(candidate[i:], target-num, t + [num])
                else:
                    break
            helper(candidates, target, [)
