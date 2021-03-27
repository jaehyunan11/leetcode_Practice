class Solution:
    def maxArea(self, h, w, horizontalCuts, verticalCuts):

        horizontalCuts = sorted(horizontalCuts)  # O(h*log(h))
        verticalCuts = sorted(verticalCuts)  # O(w*log(h))

        # Get the max height and width, only considering the cake boundaries:
        max_w = max(h-horizontalCuts[-1], horizontalCuts[0])
        max_h = max(w-veriticalCuts[-1], veriticalCuts[0])

        for i in range(len(horizontalCuts)-1):
            max_w = max(max_w, horizontalCuts[i+1]-horizontalCuts[i])
        for i in range(len(veriticalCuts)-1):
            max_h = max(max_h, veriticalCuts[i+1]-veriticalCuts[i])
        return max_w * max_h % (10**9+7)

        # # The idea is to find the maximum gap between two adjacent horizontal cuts and the maximum gap between two adjacent vertical cuts.
        # # It is important to note that the first row/column and the last row/column should also considered as a cut by default(as done in the first two lines of code).

# So, complexity analysis is:
# 1). O(h * logh) - sorting the horizontal cuts list
# 2). O(w * logw) - sorting the vertical cuts list
# 3). O(h) - finding the max. length through sorted vertical cuts list.
# 4). O(w) - finding the max, width through sorted horizontal cuts list.

# TIME : O(h*log(h) + w*log(W)) where M is length of horizontal and N is length of verticals
# Space : O(1) no extra space to store.


h = 5
w = 4
horizontalCuts = [1, 2, 4]
veriticalCuts = [1, 3]
S = Solution()
print(S.maxArea(h, w, horizontalCuts, veriticalCuts))
