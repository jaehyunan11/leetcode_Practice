class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = left
        self.right = right

# Preorder root -> left -> right


class Solution:
    def preorderTraversal(self, root):
        if root is None:
            return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)

# TIME and Space : O(N)

#stack = [right, left]


class Solution:
    def preorderTraversal(self, root):
        stack = [root]
        result = []
        while stack:
            root = stack.pop()
            result.append(root.val)
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)
        return result
# TIME and Space : O(N)
