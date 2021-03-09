from collections import defaultdict


# class Solution:
#     def numParisDivisibleBy60(self, time):
#         # dictionary
#         # key: remainder of modulo 60
#         # value: occurence of remainder
#         residual = defaultdict(int)

#         # counter of valid paris
#         counter = 0

#         # update the dictionary of remainder
#         for t in time:

#             # remainder of t modulo 60
#             remainder = t % 60

#             # remainder of (60-t) modulo 60
#             complement_remainder = (60-t) % 60
#             print(complement_remainder)

#             # find valid pairs with current t, add corresponding pair count
#             counter += residual[complement_remainder]

#             # update residual dictionary
#             residual[remainder] += 1
#         print(residual)

#         return counter

class Solution:
    def numParisDivisibleBy60(self, time):
        count = 0
        elements = [0] * 60

        for i in time:
            count += elements[-i % 60]
            print(count)
            elements[i % 60] += 1
            print(elements)

        return count


S = Solution()
time = [30, 20, 150, 100, 40]
print(S.numParisDivisibleBy60(time))
