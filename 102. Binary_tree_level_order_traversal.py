class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = left
        self.right = right


# generate queue and append root to the queue
# generate empty list of next_queue, level, result.
# iterate through the number of nodes in the queue if it is existed.
# append the root.val to level
# append root.left and right to the next_queue if they are existed.
# append level in the result.
# reset the level
# move next_queue to queue
# reset the next_queue
# keep iterate until queue is empty.
# if queue is empty then return result


class Solution:
    def levelOrder(self, root: TreeNode):
        if root is None:
            return []
        queue = [root]
        next_queue = []
        level = []
        result = []
        while queue != []:
            for root in queue:
                level.append(root.val)
                if root.left is not None:
                    next_queue.append(root.left)
                if root.right is not None:
                    next_queue.append(root.right)
            result.append(level)
            level = []  # reset the level
            queue = next_queue
            next_queue = []  # reset next_queue
        return result


1. queue = []
next_queue = []
level = []
result[[1], [2, 3], [4, 5, 6, 7]]
2.
