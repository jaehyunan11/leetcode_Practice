"""
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

"""


from collections import deque


class Solution:
    def coinChange(self, coins, amount):
        if amount == 0:
            return 0

        seen = set()
        # curr, count
        queue = [[0, 0]]

        while queue:
            curr, count = queue.pop(0)

            if count != 0 and curr == amount:
                return count

            for c in coins:
                if curr + c not in seen and curr <= amount:
                    queue.append([curr + c, count+1])
                    seen.add(curr+c)
        return -1

# TIME : O(N)
# SPACE : O(N)

        # visited = set()
        # queue = deque([(amount, 0)])  # remainder, coin_count
        # coins.sort(reverse=True)  # O(logN)

        # while queue:  # bfs / shortest path
        #     remainder, coin_count = queue.popleft()
        #     if remainder not in visited:
        #         if remainder == 0:
        #             return coin_count
        #         if remainder < 0:
        #             continue
        #         for coin in coins:
        #             queue.append((remainder-coin, coin_count+1))
        #         visited.add(remainder)
        # return -1
        # TIME : O(NLogN)
        # SPACE : O(N)


S = Solution()
coins = [1, 2, 5]
amount = 11
print(S.coinChange(coins, amount))
