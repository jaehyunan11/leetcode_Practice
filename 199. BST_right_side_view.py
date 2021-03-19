# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        # Go through level by level and return right most node val
        result = []
        level = []
        queue = [root]
        while queue and root is not None:
            for node in queue:
                # node.left is existed then append node.left into level
                if node.left:
                    level.append(node.left)
                # node.right is existed then append node.right val into level
                if node.right:
                    level.append(node.right)
            # append last val of the node
            result.append(node.val)
            # move value in the level into queue
            queue = level
            # reset the level
            level = []
        return result


def levelOrderBottom(self, root):
    deque, ret = collections.deque(), []
    if root:
        deque.append(root)
    while deque:
        level, size = [], len(deque)
        for _ in range(size):
            node = deque.popleft()
            level.append(node.val)
            if node.left:
                deque.append(node.left)
            if node.right:
                deque.append(node.right)
        ret.append(level)
    return ret[::-1]
