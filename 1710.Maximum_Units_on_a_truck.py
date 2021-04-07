class Solution:
    def maximumUnits(self, boxTypes, truckSize):
        # number of boxes, number of units per box
        ans = 0
        boxTypes.sort(reverse=True, key=lambda x: x[1])
        # loop boxTypes
        for count, units in boxTypes:
            if count < truckSize:
                ans += count * units
                truckSize -= count
            else:
                return ans + truckSize * units
        return ans
        # if number of box < trucksize
        # ans += num boxes * num of unit per box
        # trucksize -= num boxes
        # else
        # return ans + trucksize * number of units per box
        # return ans

# TIME : O(NLog(N)) since we sored the boxtype Log(N) and iterate each box by N
# Space : O(1) no extra space is used.


S = Solution()
boxTypes = [[1, 3], [2, 2], [3, 1]]
truckSize = 4
print(S.maximumUnits(boxTypes, truckSize))
