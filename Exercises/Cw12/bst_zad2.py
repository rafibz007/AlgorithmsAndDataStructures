"""
Znajduje minimum w drzewie, oraz tworze sobie zmienna suma
Nastepnie znajduje nastepnika tak dlugo jak dam rade i dodaje wartosc pola do sumy
"""

class BNode:
    def __init__(self):
        self.value = None
        self.key = None
        self.parent = None
        self.left = None
        self.right = None




def bst_min(root):
    while root.left is not None:
        root = root.left
    return root


def next(root):
    if root.right is not None:
        return bst_min(root.right)

    child = root
    root = root.parent
    while root is not None and root.right is not None and root.right.key == child.key:
        child = root
        root = root.parent

    return root


def sum_of_bst( root ):
    root = bst_min( root )
    sum = 0
    while root is not None:
        sum += root.value
        root = next(root)

    return sum