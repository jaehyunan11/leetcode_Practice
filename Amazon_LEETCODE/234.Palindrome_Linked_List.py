class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head):
        vals = []
        current_node = head
        while current_node is not None:
            vals.append(current_node.val)
            current_node = current_node.next
        return vals == vals[::-1]

# TIME : O(N) where n is the number of nodes in the Linked List
# SPACE : O(N) where n is the number of nodes in the Linked List.
# We are making an Array List and adding nn values to it.
