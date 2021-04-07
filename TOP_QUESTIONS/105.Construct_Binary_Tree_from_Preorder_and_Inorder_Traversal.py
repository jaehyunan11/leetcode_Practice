class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

        # for the inorder array
    # going to the left, we want all nodes to the left of the root. that is inorder[:root_index]
    # going to the right, we want all nodes to the right of the root. that is inorder[root_index + 1:]

# for the preorder array
    # going to the left, we want all nodes that could eventually become a root, for a left subtree.
    # going to the right, we want all nodes that could eventually become a root, for a right subtree.

        # preorder traversal provides us with the placement of the root
        # inorder traversal provides us with the placement of the left and right children


class Solution:
    def buildTree(self, preorder, inorder):
        map_inorder = dict()
        for idx, val in enumerate(inorder):
            map_inorder[val] = idx
        print(map_inorder)

        def buildTreeUtil(left, right):
            if left > right:
                return None
            root = TreeNode(preorder.pop(0))
            mid = map_inorder[root.val]
            leftNode = buildTreeUtil(left, mid-1)
            print(leftNode)
            rightNode = buildTreeUtil(mid+1, right)
            root.left, root.right = leftNode, rightNode
            return root
        return buildTreeUtil(0, len(preorder)-1)


S = Solution()
preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
print(S.buildTree(preorder, inorder))
