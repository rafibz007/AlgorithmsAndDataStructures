class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.f = None
        self.g = None


def path( node ):
    return max( f(node), g(node) )

#f - maksymalna sciazka konczaca sie w wierzcholku node
#g - maksymalna sciezka zawarta w podrzewie node (moze przez niego przechodzic)
def g(node):
    if node is None: return 0
    if node.g is not None: return node.g

    node.g = max( 0, g(node.left), g(node.right), f(node.left)+f(node.right)+node.val, f(node) )
    return node.g

def f(node):
    if node is None: return 0
    if node.f is not None: return node.f

    node.f = max( 0, f(node.left) + node.val, f(node.right) + node.val )
    # node.g = max( 0, g(node.left), g(node.right), f(node.left)+f(node.right)+node.val )

    return node.f



f0 = Node(10)
f1 = Node(7)
f2 = Node(-5)
f3 = Node(8)
f4 = Node(-100)
f5 = Node(2)
f6 = Node(1)
f7 = Node(-7)
f8 = Node(20)
f9 = Node(7)
f10 = Node(-5)
f11 = Node(1)
f12 = Node(-4)

f0.left = f1
f0.right = f2

f1.left = f3

f3.left = f6
f3.right = f7

f6.left = f10

f10.left = f12

f7.right = f11

f2.left = f4
f2.right = f5

f5.left = f8
f5.right = f9

print(path(f0))

