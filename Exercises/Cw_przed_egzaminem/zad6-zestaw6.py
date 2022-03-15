"""

f(p) - najbardziej wartosciowa sciezka, konczaca sie na wierzcholku p w danych poddrzewie
g(p) - najbardziej wartosciowa sciezka w danych poddrzewie (nie musi zawierac p, ale moze)

f(p) = max( f(p.child)+p.val, p.val )
g(p) = max( f(p), f(p.child1) + f(p.child2) + p.val, g(p.child), 0 )

"""

class Node:
    def __init__(self, val):
        self.val = val
        self.child = []
        self.f = None
        self.g = None

def best_path(T):

    def f(p):

        if p is None: return 0

        if p.f is not None:
            return p.f

        best = p.val
        for child in p.child:
            best = max( best, f(child)+p.val )

        p.f = best
        return p.f


    def g(p):

        if p is None: return 0

        if p.g is not None:
            return p.g

        best = f(p)

        child1 = None
        for child in p.child:
            best = max(best, g(child))
            if f(child) > f(child1):
                child1 = child

        child2 = None
        for child in p.child:
            if f(child) > f(child2) and child != child1:
                child2 = child

        best = max( best, f(child1)+f(child2)+p.val, 0 )
        p.g = best
        return p.g


    return g(T)


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

f0.child.append(f1)
f0.child.append(f2)

f1.child.append(f3)

f3.child.append(f6)
f3.child.append(f7)

f6.child.append(f10)

f10.child.append(f12)

f7.child.append(f11)

f2.child.append(f4)
f2.child.append(f5)

f5.child.append(f8)
f5.child.append(f9)

print(best_path(f0))



