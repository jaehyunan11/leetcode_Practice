class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        # Tree Node Value
        self.value = value
        # Left Child
        self.left = left
        # Right Child
        self.right = right

    def add(self, value):
        # If value is existed in Tree Node
        if self.value:
            # Compare with input value and value in Tree Node
            if value < self.value:
                # Check If self.left is None
                if self.left is None:
                    # Create TreeNode and add value in self.left.
                    self.left = TreeNode(value)
                else:
                    # If TreeNode is existed, add input value in self.left
                    self.left.add(value)
                    # Compare with input value and value in Tree Node
            elif value > self.value:
                # Check If self.right is None
                if self.right is None:
                    # Create TreeNode and add value in self.left.
                    self.right = TreeNode(value)
                else:
                    
                    self.right.add(value)
        else:
            self.value = value

    # Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.value)
        if self.right:
            self.right.PrintTree()


root = TreeNode(27)
root.add(14)
root.add(35)
root.add(31)
root.add(10)
root.add(19)

root.PrintTree()
