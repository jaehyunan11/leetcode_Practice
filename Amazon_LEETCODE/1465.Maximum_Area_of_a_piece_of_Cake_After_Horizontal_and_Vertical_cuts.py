class Solution:
    def maxArea(self, h, w, horizontalCuts, verticalCuts):
        # The idea is to find the maximum gap between two adjacent horizontal cuts and the maximum gap between two adjacent vertical cuts.
        # It is important to note that the first row/column and the last row/column should also considered as a cut by default(as done in the first two lines of code).
        horizontalCuts = sorted(horizontalCuts)
        verticalCuts = sorted(verticalCuts)

        # checking the gap between last horizontal cut and last buttommost cuts
        max_w = max(h-horizontalCuts[-1], horizontalCuts[0])
        max_h = max(w-verticalCuts[-1], verticalCuts[0])

        for i in range(len(horizontalCuts)-1):
            max_w = max(max_w, horizontalCuts[i+1]-horizontalCuts[i])

        for j in range(len(verticalCuts)-1):
            max_h = max(max_h, verticalCuts[j+1]-verticalCuts[j])

        return max_w * max_h % (10**9+7)

# TIME : O(hLog(h) + wLog(w)) since we first sorted cuts and iternate 2(N) to find max
# Space : O(1) We are not creating new data structure whose depends on input


S = Solution()
h = 5
w = 4
horizontalCuts = [1, 2, 4]
verticalCuts = [1, 3]
print(S.maxArea(h, w, horizontalCuts, verticalCuts))
