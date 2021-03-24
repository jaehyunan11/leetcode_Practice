from heapq import heappush, heappop, heapify

heap = []

# heappush(heap, 2)
# heappush(heap, 4)
# heappush(heap, 7)
# heappush(heap, 1)
# heappush(heap, 3)
# heappush(heap, 11)
# heappush(heap, 9)
# heappop(heap)
# heapify(heap)

# print(heap)

heapData = [10, 50, 60, 20, 70]
heapify(heapData)
print(heapData)
heappush(heapData, 30)
print(heapData)
heappop(heapData)
print(heapData)
