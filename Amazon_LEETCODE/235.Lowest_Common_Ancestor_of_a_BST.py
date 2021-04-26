# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        # both p, q value < root then node = node.left
        # both p, q value > root then node = node.right
        # return node
        p_val = p.val
        q_val = q.val

        node = root

        while node:
            # value of parent
            parent_val = node.val

            if p_val > parent_val and q_val > parent_val:
                node = node.right
            elif p_val < parent_val and q_val < parent_val:
                node = node.left
            else:
                return node
# TIME : O(N) where N is the number of node in the BST
# SPACE : O(1) since we are not using algorithm to use extra space
