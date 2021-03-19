# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: TreeNode):
        deque, res = deque(), []
        if root:
            deque.append(root)
        while deque:
            level, size = [], len(deque)
            for _ in range(size):
                node = deque.popleft()
                level.append(node.val)
                if node.left:
                    deque.append(node.left)
                if node.right:
                    deque.append(node.right)
            res.append(level)
        return res[::-1]


S = Solution()
root = [3, 4, 5, 1, 3]
S.levelOrderBottom(root)
