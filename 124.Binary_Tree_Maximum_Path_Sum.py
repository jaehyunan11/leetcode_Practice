# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        # set max to -inf since we could have negative value in the tree
        self._max = float('-inf')

        # MaxPathSumHelper Function
        def MaxPathSumHelper(node):
            # base case
            if not node:
                return 0
            # if not node then return 0
            if not node.left and node.right:
                self._max = max(self._max, nodel.val)
                return node.val
            # if there are no children then compare the max value between node.val and self._max

            left = MaxPathSumHelper(node.left)
            right = MaxPathSumHelper(node.right)
            # travese left and right node

            # if node is negative then change it to 0
            left = 0 if left < 0 else left
            right = 0 if right < 0 else right

            # check if node + two children are self._max
            # if it is then replace the self._max
            self._max = max(self._max, node.val + left + right)

            # when a node gives its value to the parent, it should give the path with larger value
            return max(left, right) + node.val

            # add node.val + left + right and compare with self._max
            # update the largest value from those two values

        maxPathSumHelper(root)
        return self._max
# TIME : O(N) where n is number of node tree and we visit each node not more than 2 times
# Space : O(H) where h is height of the node tree

        # # set max since we could have negative number in tree
        # self._max = -float('inf')

        # def traverse(node):
        #     if not node:
        #         return 0
        #     # recursive call left and right
        #     left = traverse(node.left)
        #     right = traverse(node.right)
        #     # we keep traversing upwards
        #     # we want to make sure we only have single line going down instead of multiple branch that could end of our result since it is not eligiable
        #     local_max = max(node.val, node.val + max(left, right))
        #     # we cross the path and we are done
        #     self._max = max(self._max, local_max, node.val+left+right)
        #     return local_max
        # return max(traverse(root), self._max)

# TIME : O(N) where N is number of node in the tree
# Space : O(H) where H is height of the tree since we are doing recursive call to touch every node in the tree
