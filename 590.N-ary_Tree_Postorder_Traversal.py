class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root):
        # base
        if root is None:
            return []
        # stack with root and output
        stack, output = [root], []
        while stack:
            node = stack.pop()
            if node is not None:
                output.append(node.val)
            for child in root.children:
                stack.append(child)
        print(output)
        return output[::-1]


# TIME : O(N) where N is the number of node
# space : O(N) size of the tree
