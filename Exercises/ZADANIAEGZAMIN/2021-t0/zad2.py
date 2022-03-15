"""

X = [ f(node, len), g(node, len) ]
f - tablica zawierajaca mozliwie najlepsza sume dla kazdego spojnego poddrzewa kazdej mozliwej dlugosci zawartego w
poddrzewie zaczynajacym sie na node oraz zawierajaca krawedz wychodzaca od node

g - tablica zawierajaca mozliwie najlepsza sume dla kazdego spojnego poddrzewa kazdej mozliwej dlugosci zawartego w
poddrzewie zaczynajacym sie na node - ale nie musi zawierac krawedzi zawartej w node

f(node, len) = max{  f(node.right, len-j) + node.rightval(if len-j > 0) + f(node.left, j) + node.leftval(if j>0) }
g(node, len) = max{  f(node, len), g(node.left, len), g(node.right, len)  }

f(leaf, 0) = 0 dla kazdego m
g(leaf, 0) = 0 dla kazdego m

f(leaf, m) = -inf dla kazdego m
g(leaf, m) = -inf dla kazdego m

Jesli jakis node nie istnieje, to f(node, m) = -inf, aby biorac max() nigdy nie wzielo tej okolicznosci pod uwage

"""

class Node:
    def __init__(self):
        self.left = None
        self.leftval = 0
        self.right = None
        self.rightval = 0
        self.X = None



def valueableTree( T, k ):

    def f(node, len):
        nonlocal k, inf

        if node is None: return -inf

        if node.X is None:
            node.X = [ [-inf]*(k+1) for _ in range(2) ]
            node.X[0][0] = 0
            node.X[1][0] = 0

        if node.X[0][len] > -inf: return node.X[0][len]

        best = max( f(node.left, len-1)+node.leftval, f(node.right, len-1)+node.rightval )

        for j in range(1,len):
            best = max( best, f(node.left, len-j-1)+node.leftval + f(node.right, j-1)+node.rightval )

        node.X[0][len] = best
        return node.X[0][len]


    def g(node, len):
        nonlocal k, inf

        if node is None: return -inf

        if node.X is None:
            node.X = [ [-inf]*(k+1) for _ in range(2) ]
            node.X[0][0] = 0
            node.X[1][0] = 0

        if node.X[1][len] > -inf: return node.X[1][len]

        node.X[1][len] = max(f(node, len), g(node.left, len), g(node.right, len))
        return node.X[1][len]

    inf = float("inf")
    return max( f(T, k), g(T, k) )


A = Node()
B = Node()
C = Node()
D = Node()
E = Node()
F = Node()
G = Node()

A.left = B
A.leftval = 1

A.right = E
A.rightval = 5

B.left = D
B.leftval = 6

B.right = C
B.rightval = 2

C.left = F
C.leftval = 8

C.right = G
C.rightval = 10

print(valueableTree(A, 3))