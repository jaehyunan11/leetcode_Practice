class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value


def insert(root, node):
    if root is None:
        root = node
        return

    if root.data < node.data:
        # go to right
        if root.right is None:
            root.right = node
        else:
            insert(root.right, node)
    else:
        # go to left
        if root.left is None:
            root.left = node
        else:
            insert(root.left, node)


def search(node, key):
    print("Current node is: ", node.data)
    if node is None:
        print("No node found")
        return None
    if node.data == key:
        print("Node found !")
        return node
    if node.data < key:
        return search(node.right, key)
    return search(node.left, key)


def minimumValue(node):
    while node.left is not None:
        node = node.left
    return node


def deleteNode(node, key):
    if node is None:
        return node
    if key < node.data:
        node.left = deleteNode(node.left, key)
    elif key > node.data:
        node.right = deleteNode(node.right, key)
    else:
        # case1 : one child
        if node.left is None:
            temp = node.right
            node = None
            return temp
        elif node.right is None:
            temp = node.left
            node = None
            return temp
        # case2 : 2 children
        temp = minimumValue(node.right)
        node.data = temp.data
        node.right = deleteNode(node.right, temp.data)
    return node


def preorder(node):
    if node is not None:
        print(node.data)
        preorder(node.left)
        preorder(node.right)


tree = Node(5)
insert(tree, Node(3))
insert(tree, Node(2))
insert(tree, Node(4))
insert(tree, Node(7))
insert(tree, Node(8))
insert(tree, Node(6))
search(tree, 8)
deleteNode(tree, 7)
# root left right
preorder(tree)
