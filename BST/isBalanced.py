class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode):
        if (not root):
            return True

        def find_height(node):
            if (not node):
                return 0
            leftHeight = find_height(node.left)
            rightHeight = find_height(node.right)
            if (leftHeight == -1 or rightHeight == -1):
                return -1
            elif (abs(leftHeight-rightHeight) > 1):
                return -1
            return 1+max(leftHeight, rightHeight)
        return find_height(root) != -1


# class Solution:
#     def height(self, root: TreeNode):
#         if not root:
#             return -1
#         return max(self.height(root.left), self.height(root.right)) + 1

#     def isBalanced(self, root: TreeNode) -> bool:
#         if not root:
#             return True

#         leftHeight = self.height(root.left)
#         rightHeight = self.height(root.right)

#         if abs(leftHeight-rightHeight) <= 1:
#             return self.isBalanced(root.left) and self.isBalanced(root.right)
#         else:
#             return False


def height(self, root: TreeNode):
    if root is None:
        return -1
    return max(self.height(root.left), self.height(root.right)) + 1
