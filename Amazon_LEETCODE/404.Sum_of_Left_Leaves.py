# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumOfLeftLeaves(self, root):
        # An empty root is one of the test cases
        if root is None:
            return 0

        def process_subtree(subtree, is_left):
            if subree.left is None and subtree.right is None:
                return subtree.val if is_left else 0

            # Recursive case : We need to add and return the result of the left and right subtrees
            total = 0
            if subtree.left:
                total += process_subtree(subtree.left, True)
            if subtree.right:
                total += process_subtree(subtree.right, False)
            return total
        return process_subtree(root, False)

# TIME : O(N) we are traversing all the trees
# SPACE : O(N)
