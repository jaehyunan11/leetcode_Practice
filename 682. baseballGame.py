class Solution:
    def calPoints(self, ops):
        # base case
        if ops == []:
            return None

        # score
        score = []

        # loop each opeations
        for op in ops:
            if op == '+':
                score.append(score[-1] + score[-2])
            elif op == 'D':
                score.append(2*score[-1])
            elif op == 'C':
                score.pop()
            else:
                score.append(int(op))
        return sum(score)


S = Solution()
ops = ["5", "2", "C", "D", "+"]
print(S.calPoints(ops))
