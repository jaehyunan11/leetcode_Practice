class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def topVivew(self, root):
        d = {}

        # create function for traversing

        def traverse(self, root, key, level):
            if root:
                # key not present in dictionary
                if key not in d:
                    d[key] = [root, level]
                # key with lesser level
                elif d[key][1] > level:
                    d[key] = [root, level]

                # traverse to left and right
                traverse(root.left, key-1, level-1)
                traverse(root.right, key+1, level+1)

        traverse(root, 0, 0)
        # print the elements in order
        for key in sorted(d):
            print(d[key][0], end="")
