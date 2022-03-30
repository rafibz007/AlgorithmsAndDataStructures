def list_to_matrix( G ):
    n = len(G)
    GG = [ [0]*n for _ in range(n) ]

    for i in range(n):
        for v in G[i]:
            GG[i][v]=1

    return GG