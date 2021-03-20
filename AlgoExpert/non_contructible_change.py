# nLogn TIME since sort input array and iternate 1 time
class Solution:
    def nonConstructibleChange(self, coins):
        # sort coins
        coins.sort()

        currentChangeCreated = 0
        for coin in coins:
            # coin is still greater than CCC + 1 then there is no way to create change
            if coin > currentChangeCreated + 1:
                return currentChangeCreated + 1
            # otherwise keep add the coin in the coins.
            currentChangeCreated += coin
        return currentChangeCreated + 1
