# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    # BFS level by level
    # if reach out to each level
    # Add rightmost node to rightside array
    def rightSideView(self, root):
        # Edge case
        if root is None:
            return []
        queue = deque([root, ])
        rightside = []

        while queue:
            level_length = len(queue)

            for i in range(level_length):
                node = queue.popleft()
                # if it's the rightmost element
                if i == level_length - 1:
                    rightside.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return rightside
# TIME : O(N) since one has to visit each node
# Space : O(H) length of the tree
