# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.valid(root, float('-inf'), flaot('inf'))

    def valid(self, node, left, right):
        # empty node BST
        if not node:
            return True
        # edge case
        if not(node.val < right and node.val > left):
            return False
        # left tree subtree has to less than parent right subtree has to be greater than parent.
        return (valid(node.left, left, node.val) and valid(
            node.right, node.val, right))
