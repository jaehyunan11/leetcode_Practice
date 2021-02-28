class Solution:
    def kClosest(self, points, K):
        points.sort(key=lambda x: x[0]*x[0] + x[1]*x[1])
        print(f"Current Points: {points}")
        return points[:K]


s = Solution()
K = 1
points = points = [[1, 3], [-2, 2]]
print(s.kClosest(points, K))
