class BNode:
    def __init__(self):
        self.value = None
        self.key = None
        self.parent = None
        self.left = None
        self.right = None
        self.amount = None



def find_i_elem( root, i ):
    left_side = 0
    if root.left is not None: left_side = root.left.amount

    right_side = 0
    if root.right is not None: right_side = root.right.amount

    #znaczy ze jest to i-ty element, bo ma i-1 mniejszych elementow
    if root.amount - right_side == i:
        return root

    #i-ty element znajduje sie po lewej stronie, bo po lewej jest wiecej niz i elementow
    if left_side >= i:
        return find_i_elem( root.left, i )

    # i-ty element znajduje sie po prawej stronie, ale teraz szukam (root.amount - left_side - 1) elemntu
    # poniewaz odrzucam left_side + 1 elemntow mniejszych i szukam wsord wiekszych (root.amount - left_side - 1) elemntu
    if root.amount - left_side - 1 > 0 and right_side > 0:
        return find_i_elem( root.right, root.amount - left_side - 1 )

    return None


def which_in_turn( root, _k=1 ):

    if root.parent is not None:
        if root.parent.left == root:
            return which_in_turn(root.parent, _k)
        if root.parent.right == root:

            left_side = 0
            if root.parent.left is not None: left_side = root.left.amount

            return which_in_turn(root.parent, _k+left_side+1)

    return _k