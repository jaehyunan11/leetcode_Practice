class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        type l1 : ListNode
        type l2 : ListNode
        rtype : ListNode
        """

        dummy = ListNode(0)
        tail = dummy

        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        return dummy.next


S = Solution()
l1 = [1, 2, 4]
l2 = [1, 3, 4]
print(S.mergeTwoLists(l1, l2))
