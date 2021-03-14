class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # Base Case
        # if both reached end then return True
        if p == None and q == None:
            return True
        # if one of them are None return False
        elif p == None or q == None:
            return False

        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return False

# Time complexity : O(N)
# Space Complexity : O(N) Height
