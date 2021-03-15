# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def minDepth(self, root):
        # base case tree is empty
        if not root:
            return 0
        q = collections.deque()
        # First append root and depth of 1
        q.append((root, 1))

        # loop q until it is empty.
        while q:
            # pop out first node
            self, depth = q.popleft()
            # node, depth = q.popleft()

            # In case if there is no left and right children
            if not self.left and not self.right:
                # if not node.left and not node.right:
                return depth

            # Check left child and add in the q.
            if self.left:
                q.append((self.left, depth+1))

            # Check right child and add in the q.
            if self.right:
                q.append((self.right, depth+))

    def DFS_minDepth(self, root):

        if not root:
            return 0

        if not root.left and not root.right:
            return 1

        if not root.right and root.left:
            return 1 + self.DFS_minDepth(root.left)

        if not root.left and root.right:
            return 1 + self.DFS_minDepth(root.right)

        return 1 + min(self.minDepth(root.left), self.DFS_minDepth(root.right))
