# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists):
        self.node = [1, 4, 5, 1, 3, 4, 2, 6]
        for x in sorted(self.node):
            print(sorted(self.node))


S = Solution()
lists = [1, 2, 3, 4, 5]
print(S.mergeKLists(lists))
