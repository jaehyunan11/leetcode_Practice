from collections import defaultdict
from heapq import heappop, heappush


class Solution:
    def minimumCost(self, N, connections):
        neightbor = defaultdict(list)
        for i, j, c in connections:
            neightbor[i].append((j, c))
            neightbor[j].append((i, c))
        print(neightbor)
        """
        neighbor = {
			1: (2,5),(3,6)
			2: (1,5),(3,1)
			3: (1,6),(2,1)
			}
        """
        """
        Use a minimum heap to store the cost and neighbors of the current city. 
        The minimum heap sorts the cost in ascending order. 
        So each time the neighbor pop from the heap will be the neighbor who has the least cost to the current city.
        """
        """
        mini_heap = [(cost from current city to neighbor to current city, neighbor to current city )]
        """
        res = 0
        # First start with c = 0, i = 1
        min_heap = [(0, 1)]
        visited = set()


S = Solution()
N = 3
connections = [[1, 2, 5], [1, 3, 6], [2, 3, 1]]
print(S.minimumCost(N, connections))
