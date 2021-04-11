# Tree
# A Connected
# Acyclic graph (No Cycle)
# Undirected graphs (graph whose edges are bi-directional)

# Binary Trees
# Every node in a binary tree has at most, 2 children

# Path
# Sequence of nodes connected together in a tree

# Parent:
# a node above another node connected by it's edge

# Child:
# A node below another node connected by its edge

# Root:
# The node at the top of the tree,
# There is only one root per tree and one path from the root node to any node
# A root has no parents.

# Leaf node:
# A node with no children nodes

# Tree Height:
# The number of edges on the longest downward path between the root and a leaf

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


root = Node(4)
root.left = Node(5)
root.right = Node(6)
root.left.left = Node(7)


# class TreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.children = []
#         self.parent = None

#     def add_child(self, child):
#         child.parent = self
#         self.children.append(child)

#     def get_level(self):
#         level = 0
#         p = self.parent
#         while p:
#             level += 1
#             p = p.parent
#         return level

#     def print_tree(self):
#         spaces = ' ' * self.get_level() * 3
#         prefix = spaces + "|__" if self.parent else ""
#         print(prefix + self.data)
#         if len(self.children):
#             for child in self.children:
#                 child.print_tree()


# def build_product_tree():
#     root = TreeNode("Electronics")

#     laptop = TreeNode("Laptop")
#     laptop.add_child(TreeNode("Mac"))
#     laptop.add_child(TreeNode("Surface"))
#     laptop.add_child(TreeNode("Thinkpad"))

#     cellphone = TreeNode("Cell Phone")
#     cellphone.add_child(TreeNode("iphone"))
#     cellphone.add_child(TreeNode("Google Pixel"))
#     cellphone.add_child(TreeNode("Vivo"))

#     tv = TreeNode("TV")
#     tv.add_child(TreeNode("Samsung"))
#     tv.add_child(TreeNode("LG"))

#     root.add_child(laptop)
#     root.add_child(cellphone)
#     root.add_child(tv)

#     return root


# if __name__ == '__main__':
#     root = build_product_tree()
#     # print(root.get_level())
#     root.print_tree()
#     pass
