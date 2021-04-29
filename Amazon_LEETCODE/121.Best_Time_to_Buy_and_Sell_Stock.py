class Solution:
    def maxProfit(self, prices):
        # Base Case
        if not prices:
            return 0
        # Find maxProfit and minPrice
        maxProfit = 0
        minPrice = prices[0]

        # Loop the prices
        for i in range(1, len(prices)):
            # find least number
            if prices[i] < minPrice:
                minPrice = prices[i]
            # find the maxprofit before moving forward
            elif prices[i] - minPrice > maxProfit:
                maxProfit = prices[i] - minPrice
        return maxProfit
# TIME: O(N) where N is number of prices
# SPACE : O(1) linear space and no extra space is needed.


S = Solution()
prices = [7, 1, 5, 3, 6, 4]
print(S.maxProfit(prices))
