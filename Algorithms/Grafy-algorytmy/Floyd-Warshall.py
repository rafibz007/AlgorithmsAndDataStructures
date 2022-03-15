def Floyd_Warshall( G ):
    n = len(G)
    S = [ G[i].copy() for i in range(n) ]

    for t in range(1, n):
        for u in range(n):
            for v in range(n):
                if u == v: continue
                S[u][v] = min( S[u][v], S[u][t] + S[t][v] )

    return S