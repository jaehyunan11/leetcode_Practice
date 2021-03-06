# class Solution:
#     def topKFrequent(self, nums, k):
#         self.dict = {}
#         if not nums:
#             return []
#         elif len(nums) == 1:
#             return nums[0]
#         else:
#             for num in nums:
#                 if num not in self.dict:
#                     self.dict[num] = 1
#                 else:
#                     self.dict[num] += 1
#         # insert k items into heap O(nlog(k))
#         h = []
#         from heapq import heappush, heappop
#         for key in self.dict:  # O(N)
#             heappush(h, (self.dict[key], key))
#             if len(h) > k:
#                 heappop(h)
#         res = []
#         while h:  # O(k)
#             frq, item = heappop(h)
#             res.append(item)
#         return res
from collections import Counter
from heapq import heapify, heappop


class Solution:
    def topKFrequent(self, nums, k):
        c = Counter(nums)
        pq = [(-v, k) for k, v in c.items()]

        heapify(pq)
        print(pq)
        res = []
        for i in range(0, k):
            res.append(heappop(pq)[1])
        return res


s = Solution()
nums = [1, 1, 1, 2, 2, 3]
k = 2
print(s.topKFrequent(nums, k))


# from heapq import heappush, heappop, heapify, heappushpop


# def heapsort(iterable):
#     h = []
#     for value in iterable:
#         heappush(h, value)
#     return [heappop(h) for i in range(len(h))]


# print(heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))

# h = []
# heappush(h, (5, 'Write Code'))
# heappush(h, (7, 'Release Product'))
# heappush(h, (1, 'Write Spec'))
# heappush(h, (3, 'Create Test'))
# print(h)

# li = [1, 3, 5, 7, 2, 4]
# heapify(li)
# print(li)
