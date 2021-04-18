from heapq import heappop, heappush


class Solution:
    def kClosestSort(self, points, K):
        points.sort(key=lambda x: x[0]*x[0] + x[1]*x[1])
        return points[:K]

# TIME : O(log(n))
# Space : O(1)

    def kClosestHeap(self, points, K):
        heap = []
        for i in range(len(points)):
            x = points[i][0]
            y = points[i][1]
            d = (x*x + y*y)
            heappush(heap, [d, [x, y]])
        print(heap)
        res = []
        for i in range(K):
            res.append(heappop(heap)[1])
        return res

# TIME : Inserting an item to a heap of size k take O(logK) time.
# And we do this for each item points.
# So runtime is O(N * logK) where N is the length of points.
# Space: O(K) for our heap


S = Solution()
points = [[1, 3], [-2, 2]]
K = 1
print(S.kClosestSort(points, K))
print(S.kClosestHeap(points, K))
