class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeString(self, root: TreeNode):
        if root.left is None:
            left = "lnull"
        else:
            left = self.treeString(root.left)
        if root.right is None:
            right = "rnull"
        else:
            right = self.treeString(root.right)
        return f"*{root.val} {left} {right}"

    def isSubtree(self, s, t):
        if s is None or t is None:
            return False

        str_s = self.treeString(s)
        str_t = self.treeString(t)
        if str_t in str_s:
            return True
        return False


S = Solution()
s = [3, 4, 5, 1, 2]
t = [4, 1, 2]

print(S.isSubtree(s, t))
