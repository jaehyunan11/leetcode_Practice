class Solution:
    def maxProfit(self, prices):
        # edge case
        if len(prices) == 1:
            return 0
        # max_profit
        # check difference between [day +1] - [day] of the stock price
        # keep add positive num to the max_profit
        # if difference is negative then it is 0

        max_profit = 0
        for day in range(len(prices)-1):
            max_profit += max(prices[day+1]-prices[day], 0)
        return max_profit


S = Solution()
prices = [7, 1, 5, 3, 6, 4]
print(S.maxProfit(prices))
