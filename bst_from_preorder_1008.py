class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstFromPreorder(self, preorder):
        # base case
        if not preorder:
            return None
        # Define root
        root = TreeNode(preorder[0])
        # Set i = 1 to compare root with other numbers
        i = 1
        while i < len(preorder):
            if preorder[i] > preorder[0]:
                break
            i += 1
        # Recursion for root.left which is less than root
        root.left = self.bstFromPreorder(preorder[1:i])
        # Recursion for root.right which is greater than root
        root.right = self.bstFromPreorder(preorder[i:])
        return root


s = Solution()
preorder = [8, 5, 1, 7, 10, 12]
print(s.bstFromPreorder(preorder))
