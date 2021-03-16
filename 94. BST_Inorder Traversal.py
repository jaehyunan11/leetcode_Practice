# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
            1
        /       \
       /         \
    2             3
   /   \         /   \
4       5       6    7

[4,2,5,1,6,3,7]
1 -> 2 + [1] + 3
2 -> 4 + [2] + 5
4 -> [] + [4] + []
[4,2,5,1] + [6,3,7]
3 -> 6 + [3] + 7
6 -> [] + [6] + []
 
"""


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

# stack = [1]
# result = [4, 2, 5, 1]


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        stack = []
        result = []
        while root is not None or stack != []:
            while root is not None:
                stack.append(root)
                root = root.left
            root = stack.pop()
            result.append(root.val)
            root = root.right
        return result

# TIME and Space : O(N)
