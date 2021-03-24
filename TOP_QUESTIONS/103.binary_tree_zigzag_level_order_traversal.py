class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root):
        # Create queue and root as default
        traversal_queue = [root] if root else []
        # empty path
        path = []
        # direction (default left to right)
        right_to_left = False

        while traversal_queue:

            cur_level_path, next_level_queue = [], []

            for node in traversal_queue:

                cur_level_path.append(node.val)

                if node.left:
                    next_level_queue.append(node.left)

                if node.right:
                    next_level_queue.append(node.right)

            # update the path of level order traversal
            # right_to_left is True then reserse else left to right order
            if right_to_left:
                path.append(cur_level_path[::-1])
            else:
                path.append(cur_level_path)

            # update traversal queue as next level queue
            traversal_queue = next_level_queue

            # switch direction for next level

            right_to_left = not right_to_left

        return path

# TIME : O(N) where n is number of nodes in the tree
# SPACe : O(N) where n is number of nodes in the tree
#


Solution().zigzagLevelOrder([1])
