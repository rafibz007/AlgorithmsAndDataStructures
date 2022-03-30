def matrix_to_list( G ):
    n = len(G)

    W = [ [] for _ in range( n ) ]

    for u in range( n ):
        for v in range( n ):
            if G[u][v] > 0:
                W[u].append( (v, G[u][v]) )

    return W