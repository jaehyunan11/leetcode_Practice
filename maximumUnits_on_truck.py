class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int):
        ans = 0
        boxTypes.sort(reverse=True, key=lambda x: x[1])
        for box, units in boxTypes:
            if box < truckSize:
                ans += box * units
                truckSize -= box
            else:
                return ans + truckSize * units
        return ans


O(n)
