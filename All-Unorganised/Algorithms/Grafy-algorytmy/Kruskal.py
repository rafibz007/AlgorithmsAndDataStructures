def Kruskala( G ):

    def find( x ):
        nonlocal parent
        if parent[x] != x:
            parent[x] = find( parent[x] )
        return parent[x]

    def union( x, y ):
        nonlocal rank,parent
        x = find(x)
        y = find(y)

        if x == y: return
        if rank[x] > rank[y]:
            parent[y] = x
        else:
            parent[x]=y
            if rank[x] == rank[y]: rank[y]+=1


    n = len(G)

    vertex_amount = 0
    for i in range(n): vertex_amount = max(vertex_amount, G[i][0], G[i][1])
    vertex_amount += 1

    A = []
    #FIND - UNION
    parent = [ i for i in range(vertex_amount) ]
    rank = [ 0 ]*vertex_amount

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