# m = # of edges
# n = # of nodes in tree
# # of edge is always 1 less than # of nodes

# TIME O(m+n) = O(n-1 + n) = O(n)
# SPACE O(n) hash map can be only stored n in potentional nodes.


# Key point for this problem is to find parents for all nodes and
# store them in a dictionary.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """

        # create the node to parent mpa and populate it
        nodeToParentMap = defaultdict(list)

        # Create the queue that we will use for the breadth first search
        # Add the start node to the queue
        queue = [target, ]

        # This is an undirected graph now that we can go to and from nodes
        # Before we could only go down the tree.
        # Therefore, we need a hashtable to keep track of nodes we have visited
        # so that we do not go back and revisit what has already been
        # processed and cause an infinite cycle

        visited = set()
        visited.add(target)

        # When our search starts , we are standing at distance 0
        currentDistance = 0
        while queue:

            # is this the distance we want? If so, extract and return it
            if currentDistance == K:


class Solution:
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        res = []
        seen = set()

        def findK(self, node, k):  # find the nodes with distant k
            if not node or node.val in seen:
                return
            elif k == 0:
                res.append(node.val)
                return
            seen.add(node.val)
            findk(node.left, k-1)
            findk(node.right, k-1)

        def findT(self, node):  # find the target
            if not node:
                return 0
            if node == target:
                findK(node, K)
                return 1
            d = findT(node.left) or findT(node.right)
            if d:  # if found return d+1
                findK(node, K-d)
                return d+1
            else:  # if not found, always return 0
                return 0

        findt(root)
        return res
