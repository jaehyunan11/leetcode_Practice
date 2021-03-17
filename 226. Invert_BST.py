# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root):
        if not root:
            return
        # create queue by using collections.deque
        q = collections.deque()
        # add root in the queue
        q.append(root)

        while q:
            curr = q.popleft()
            temp = curr.left
            curr.left = curr.right
            curr.right = temp
            if curr.left != None:
                q.append(curr.left)
            if curr.right != None:
                q.append(curr.right)

        return root
