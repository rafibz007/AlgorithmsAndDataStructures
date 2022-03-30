class BST_Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None


def find(root, key):
    while root is not None:
        if root.key > key:
            root = root.left
        elif root.key < key:
            root = root.right
        else:
            break
    return root


def bst_min(root):
    while root.left is not None:
        root = root.left
    return root


def bst_max(root):
    while root.right is not None:
        root = root.right
    return root


def insert(root, key, value=None):
    new_node = BST_Node()
    new_node.value = value
    new_node.key = key

    while True:
        if root.key > key and root.left is not None:
            root = root.left
        elif root.key < key and root.right is not None:
            root = root.right
        elif root.key > key:
            new_node.parent = root
            root.left = new_node
            break
        elif root.key < key:
            new_node.parent = root
            root.right = new_node
            break
        else:
            root.value = value  # return - lub to, zalezy o co nam chodzi
            break
    return


def next(root):
    if root.right is not None:
        return bst_min(root.right)

    child = root
    root = root.parent
    while root is not None and root.right is not None and root.right.key == child.key:
        child = root
        root = root.parent

    return root


def prev(root):
    if root.left is not None:
        return bst_min(root.left)

    child = root
    root = root.parent
    while root is not None and root.left is not None and root.left.key == child.key:
        child = root
        root = root.parent

    return root


def remove(root, key):
    head = root
    root = find(root, key)

    if root.right is None and root.left is None and root.parent is not None:
        root = root.parent
        if root.left.key == key:
            root.left = None
        elif root.right.key == key:
            root.right = None

    elif root.right is None and root.parent is None:
        return root.left

    elif root.left is None and root.parent is None:
        return root.right

    elif root.right is None:
        root = root.parent
        if root.left.key == key:
            root.left = root.left.left
        elif root.right.key == key:
            root.right = root.right.left

    elif root.left is None:
        root = root.parent
        if root.left.key == key:
            root.left = root.left.right
        elif root.right.key == key:
            root.right = root.right.right

    else:
        change_node = next(root)
        root.key = change_node.key
        root.value = change_node.value
        remove(root.right, root.key)

    return head
