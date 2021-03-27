from heapq import heapify, heappop, heappush


class Solution:
    def connectSticks(self, sticks):
        # The idea is always pick the smallest values of sticks and add them
        # then put them back in sticks
        print(sticks)
        heapify(sticks)
        print(sticks)

        total_cost = 0

        while len(sticks) > 1:
            first_smallest, second_smallest = heappop(sticks), heappop(sticks)
            current_cost = first_smallest + second_smallest
            heappush(sticks, current_cost)
            total_cost += current_cost
        return total_cost

# TIME : O(Nlon(n)) where n is length of sticks (log(n): heapify and n times of sticks
# space : O(N) since we will store N element in our priority queue


S = Solution()
sticks = [2, 4, 3]
print(S.connectSticks(sticks))
