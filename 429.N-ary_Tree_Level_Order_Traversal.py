from collections import deque


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node'):
        # No root means maxDepth is 0
        if not root:
            return 0
        # set nodes which is queue
        nodes = deque()
        # insert root and initial depth which is 1
        nodes.append((root, 1))
        # set max_depth = 0
        max_depth = 0
        # while loop if nodes are existed
        while nodes:
            # set curr node and depth
            curr, curr_depth = nodes.popleft()
            # set curr_depth is max_depth
            max_depth = curr_depth
            # if curr node and its children is existed:
            if curr.children:
                # loop each child
                for child in curr.children:
                    # append in the node queue
                    nodes.append((child, curr_depth+1))
        return max_depth

        # if root is None:
        #     return []
        # output = []
        # queue = [root]
        # while queue:
        #     level = []
        #     for _ in range(len(queue)):
        #         node = queue.pop(0)
        #         level.append(node.val)
        #         queue.extend(node.children)
        #     result.append(level)
        # return output

# TIME : O(N) where N is number of node. Each node is getting added to the queue. Remove from queue and added to the result
# exactly one
# Space : O(N) we are using a queue to keep track of nodes.
