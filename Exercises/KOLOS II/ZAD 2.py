from collections import deque

def enlarge(G, s, t):

    n = len(G)
    Q = deque()
    parent = [None]*n
    visited = [False]*n
    distance = [0]*n

    Q.append(s)
    visited[s] = True
    while Q:
        u = Q.popleft()
        print(u)
        for v in G[u]:
            print(Q)
            # if v == t: pass

            if not visited[u]:
                distance[v] = distance[u]+1
                visited[u] = True
                parent[v] = u
                Q.append(u)

    print(distance)


    return None

G = [ [1, 2],
[0, 2],
[0, 1] ]
enlarge(G, 0, 2)