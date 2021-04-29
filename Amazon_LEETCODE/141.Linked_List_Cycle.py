# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head):
        nodes_seen = set()
        while head is not None:
            # if head is seen then it is a cycle return True
            if head is nodes_seen:
                return True
            nodes_seen.add(head)
            head = head.next
        return False

# TIME :O(N) number of node that we have
# Space : O(N) The space depends on the number of elements added to the hash table, which contains at most nn elements.
