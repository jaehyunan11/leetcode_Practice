import heapq


class MedianFinder:

    # lower part - Max heap
    # upper part - Min heap
    # the diff between heaps length can't be greater than 1

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lowerhalf = []   # store the small half, top is the largest in the small part
        self.upperhalf = []   # store the large half, top is the smallest in the large group

    def addNum(self, num):
        # The case for the first element, just add to the maxheap
        if len(self.lowerhalf) == 0:
            heapq.heappush(self.lowerhalf, -num)
            return

        # Now choose where to add the new element

        # If it is less than or equal the top of max heap, it can be accomodated under it else go to min heap
        if num <= -self.lowerhalf[0]:
            heapq.heappush(self.lowerhalf, -num)  # Go to the max Heap
            # (-ve sign because to implement max heap using the default heapq in python, we need to negate the values)
        else:
            heapq.heappush(self.upperhalf, num)  # go to min heap

        # Adjusting the balance

        # if the lowerhalf heap has more elements
        if len(self.lowerhalf) > len(self.upperhalf) == 2:
            heapq.heappush(self.upperhalf, -heapq.heappop(self.lowerhalf))
        # if the upperhalf heap has more elements

        elif len(self.upperhalf) - len(self.lowerhalf) == 2:
            heapq.heappush(self.lowerhalf, -heapq.heappop(self.upperhalf))

    def findMedian(self):
        # if both heaps have same number of elements return the avg
        # if not, then the root of the one with more elements, is the answer
        if len(self.lowerhalf) == len(self.upperhalf):
            return (-self.lowerhalf[0] + self.upperhalf[0]) / 2.0
        elif len(self.lowerhalf) > len(self.upperhalf):
            return -float(self.lowerhalf[0])
        else:
            return float(self.upperhalf[0])

# TIME : log(n) (insert) + log(n) (balancing)


num = [1, 3, 5]
S = MedianFinder()
S.addNum(num)
print(MedianFinder().findMedian())
