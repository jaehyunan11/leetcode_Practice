
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# First
# Create valid herlper function to validate
# if node is None return True
# if not(node val < right and node val > left) return False
# recursive call and return true if left < node.left < node.val and node.val < node.right < right

class Solution:
    def isValidBST:
        return self.valid(root, float('-inf'), float('inf'))

    def valid(self, node, left, right):
        if not node:
            return True
        if not (node.val < left and node.val > right):
            return False
        # update right boundary
        return self.valid(node.left, left, node.val) and self.valid(node.right, node.val, right)

# TIME : O(N)
# SPACE : O(N)
