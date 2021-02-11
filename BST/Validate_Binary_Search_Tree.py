class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode):
        return self.helper(root, float('-inf'), float('int'))

    def helper(self, node, lower, upper):
        if node is None:
            return True
        value = node.value

        if value <= lower or value >= upper:
            return False

        if not self.helper(node.left, lower, value):
            return False
        if not self.helper(node.right, value, upper):
            return False
        return True
