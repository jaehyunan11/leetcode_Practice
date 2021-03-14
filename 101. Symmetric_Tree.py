class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root):
        # base case
        if not root:
            return True
        return self.ismirror(root.left, root.right)

    def ismirror(self, leftroot, rightroot):
        # case 1 (not leftroot and rightroot)
        if not leftroot and rightroot:
            return True
        # case 2 (leftroot and rightroot)
        if leftroot and rightroot:
            # case leftroot.val == rightroot.val
            if leftroot.val == rightroot.val:
                # check1 leftroot.left == rightroot.right
                return self.ismirror(leftroot.left, rightroot.right) and self.ismirror(leftroot.right, rightroot.left)
                # check2 leftroot.right == rightroot.left
            # return False
        return False

# Time Complexity : O(N)
# Space Complexity : O(N) Nth height


S = Solution()
root = [1, 2, 2, 3, 4, 4, 3]
print(S.isSymmetric(root))
