from zad1testy import runtests
from collections import deque

def best_root( L ):

    def BFS(L, s):
        n = len(L)
        visited = [False] * n
        parent = [None]*n
        inf = float("inf")
        distance = [inf for _ in range(n)]

        queue = deque()

        queue.append(s)
        visited[s] = True
        distance[s] = 0

        while queue:
            u = queue.popleft()
            for v in L[u]:
                if not visited[v]:
                    parent[v] = u
                    distance[v] = distance[u]+1
                    visited[v] = True
                    queue.append(v)

        max_index = 0
        for i in range( n ):
            if distance[i] > distance[max_index]: max_index = i

        return max_index, parent

    D1, _ = BFS(L, 0)
    D2, parent = BFS(L, D1)

    # print(parent, distance, D2, D1)

    u = D2
    diameter = [u]
    while u != D1:
        u = parent[u]
        diameter.append(u)

    return diameter[ len(diameter)//2 ]

# if __name__ == '__main__':
#
#     L = [
#         [2],
#         [2],
#         [0, 1, 3],
#         [2, 4],
#         [3,5,6],
#         [4],
#         [4]
#     ]
#     print(best_root(L))

runtests( best_root )
