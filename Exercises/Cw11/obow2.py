from math import inf

def list_to_matrix( G ):
    n = len(G)
    GG = [ [inf]*n for _ in range(n) ]

    for i in range(n):
        for v in G[i]:
            GG[i][v]=1

    return GG


def Floyd_Warshall( G ):
    n = len(G)
    S = [ G[i].copy() for i in range(n) ]
    GG = [ [inf]*n for _ in range(n) ]

    for t in range(1, n):
        for u in range(n):
            for v in range(n):
                if u == v: continue
                S[u][v] = min( S[u][v], S[u][t] + S[t][v] )
                if S[u][v] < inf:
                    GG[u][v] = 1

    return GG


G = [ [1,2],
      [2],
      [3],
      [],
      [5],
      [6],
      [4]]

print(Floyd_Warshall(list_to_matrix(G)))
