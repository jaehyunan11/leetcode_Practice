class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        # Tree Node Value
        self.value = value
        # Left Child
        self.left = left
        # Right Child
        self.right = right

    def PrintTree(self):
        print(self.value)


class Solution:
    def searchBST(self, root: TreeNode, val: int):
        pass


root = TreeNode(27)
root.PrintTree()
