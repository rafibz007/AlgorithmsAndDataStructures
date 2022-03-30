from collections import deque

def spojne_skladowe( G ):

    n = len(G)
    visited = [False]*n
    Q = deque()
    counter = 0

    for v in range(n):
        if not visited[v]:
            counter += 1
            Q.append(v)
            visited[v] = True
        while Q:
            u = Q.popleft()
            for w in G[u]:
                if not visited[w]:
                    visited[w] = True
                    Q.append(w)

    return counter

G = [ [1, 2],
      [0, 2],
      [0,1],
      [4,6],
      [3,5],
      [4,6],
      [3,5],
      []
]
print(spojne_skladowe(G))