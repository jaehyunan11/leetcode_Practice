# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):

        # l1, l2, carry
        # l1 then carry += l1.val
        # then l1 = l1.next
        # l2 then carray += 12. val
        # l2 = l2.next
        # cur.next = ListNode(carry%10)
        # cur = cur.next
        # carry //=10
        # return dummy.next
        dummy = cur = ListNode(0)
        carry = 0

        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            elif l2:
                carray += l2.val
                l2 = l2.next
            cur.next = ListNode(carry % 10)
            cur = cur.next
            carry //= 10  # this will add with either l1 or l2
        return dummy.next

# TIME : O(max(m,n)) m and n represnts the length of l1 and l2
# SPACE : O(max(m,n)) The length of the new list is at most max(m,n) + max(m,n)+1.
