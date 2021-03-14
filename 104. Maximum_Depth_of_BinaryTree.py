# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # base case

        if not root:
            return 0
        left_maxDepth = self.maxDepth(root.left)
        right_maxDepth = self.maxDepth(root.right)
        return max(left_maxDepth, right_maxDepth) + 1


s = Solution()
root = [3, 9, 20, 15, 7]
print(s.maxDepth(root))
