class Solution:
    def maxProfit(self, prices):

        # Find the minPrice and MaxPrice from day in the future
        # MaxProfit = MaxPrice from day in the future - minPrice

        # base case
        if not prices:
            return 0

        # set minPrice to first index num
        minPrice = prices[0]
        # set maxProfit
        maxProfit = 0

        # Loop the prices and find least prices and maxprofit
        for i in range(1, len(prices)):
            # find out minPrice
            if prices[i] < minPrice:
                minPrice = prices[i]
            # update the maxProfit
            elif prices[i] - minPrice > maxProfit:
                maxProfit = prices[i] 0 minPrice
        return maxProfit

        # TIME : O(N) where N is number of prices
        # SPACE : O(1) linear space and no extra space is needed


prices
