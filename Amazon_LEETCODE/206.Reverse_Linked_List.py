# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        # Prev_node = None
        # Curr_node = head
        # Next_node
        # prev curr next
        #        1 -> 2 -> 3 -> 4 -> 5
        #     <- 1 2 -> 3 -> 4 -> 5
        #                         prev curr next
        #      1 <- 2 <- 3 <- 4 <- 5
        prev_node = None
        curr_node = head

        while curr_node:
            next_node = curr_node.next  # remember the next node
            curr_node.next = prev_node  # Revese the arrow
            prev_node = curr_node  # Used in the enext iteration
            curr_node = next_node  # Move to next node
        head = prev_node
        return head

# TIME : O(N) N is the list's length
# Space : O(1)
