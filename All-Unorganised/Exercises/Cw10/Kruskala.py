from queue import PriorityQueue

def Kruskala_v1( G ):

    def find( x ):
        nonlocal parent
        if parent[x] != x:
            parent[x] = find( parent[x] )
        return parent[x]

    def union( x, y ):
        x = find(x)
        y = find(y)

        if x == y: return
        if rank[x] > rank[y]:
            parent[y] = x
        else:
            parent[x]=y
            if rank[x] == rank[y]: rank[y]+=1


    n = len(G)
    A = [ [] for _ in range(n) ]
    #FIND - UNION
    parent = [ i for i in range(n) ]
    rank = [ 0 ]*n

    for i in range(n): G[i].sort(key=lambda x: x[1])
    Q = PriorityQueue()

    #print(G)

    for i in range( n ): Q.put( (G[i][0][1], i, 0) )

    while not Q.empty():
        edge, u, index = Q.get()
        v = G[u][index][0]

        if index+1 < len(G[u]): Q.put( (G[u][index+1][1], u, index+1) )

        x = find(u)
        y = find(v)

        if x != y:
            union( x, y )
            A[u].append( (v, G[u][index][1]) )
            A[v].append( (u, G[u][index][1]) ) #jesli graf nieskierowany

    return A

def Kruskala_v2( G ):

    def find( x ):
        nonlocal parent
        if parent[x] != x:
            parent[x] = find( parent[x] )
        return parent[x]

    def union( x, y ):
        x = find(x)
        y = find(y)

        if x == y: return
        if rank[x] > rank[y]:
            parent[y] = x
        else:
            parent[x]=y
            if rank[x] == rank[y]: rank[y]+=1


    n = len(G)
    A = []
    #FIND - UNION
    parent = [ i for i in range(n) ]
    rank = [ 0 ]*n

    G.sort( key=lambda x:x[2] )
    #print(G)

    for i in range(n):
        u,v,w = G[i]

        x = find(u)
        y = find(v)

        if x != y:
            union( x, y )
            A.append( (u,v,w) )
            A.append( (v,u,w) ) # jesli nieskierowany

    return A

def list_to_list( G ):
    A = []
    for u in range(len(G)):
        for v,w in G[u]:
            A.append( (u,v,w) )
    return A


G = [[(1,1), (5,7)],
     [(0,1),(2,12),(3,4),(5,8)],
     [(1,12),(3,6),(5,3)],
     [(1,4),(2,6),(4,5)],
     [(3,5),(5,2)],
     [(0,7),(1,8),(2,3),(4,2)]]

print(Kruskala_v1(G))

L1 = list_to_list(Kruskala_v1(G))
L2 = Kruskala_v2(list_to_list(G))
L1.sort()
L2.sort()
print(L1)
print(L2)


