class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution():
    def reverseList(self, head):
        # 1) Case 1 (no head)
        if not head:
            return None
        # 2) Case 2 (There is only 1 head)
        if not head.next:
            return head

        # 3) Set Prev node to None
        prev_node = None

        # 4) Loop curr_node
        while head:
            temp = head
            head = head.next
            temp = prev
            prev = temp
        return prev

        # next_node = curr_node.next  # Remember the next node
        # curr_node.next = prev_node  # Reverse curr.next to prev
        # prev_node = curr_node  # Used in the next iteration
        # curr_node = next_node  # Move to next node

        # head = prev_node
        # return head


s = Solution()
head = [1, 2, 3, 4, 5]
print(s.reverseList(head))
