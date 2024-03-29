"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root is None:
            return
        result = []
        stack = []
        stack.append(root)
        while stack:
            #
            root = stack.pop()
            result.append(root.val)
            for child in root.children[::-1]:
                stack.append(child)
        return result

# TIME : O(N) where N is the number of node
# space : O(N) size of the tree