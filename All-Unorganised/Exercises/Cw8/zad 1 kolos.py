from collections import deque
def to_port( M, T ):
    n = len(M)
    visited = [ [False]*n for _ in range(n) ]
    Q = deque()

    Q.append( (0, 0) )
    visited[0][0] = True

    neighbours = [ [-1,0], [0,-1], [1,0], [0,1] ]

    while Q:
        u = Q.popleft()
        for ngh in neighbours:
            if not 0 <= u[0]+ngh[0] < n or not 0 <= u[1]+ngh[1] < n: continue
            if not visited[ u[0]+ngh[0] ][ u[1]+ngh[1] ] and M[ u[0]+ngh[0] ][ u[1]+ngh[1] ]>T:
                visited[u[0] + ngh[0]][u[1] + ngh[1]] = True
                Q.append( (u[0] + ngh[0], u[1] + ngh[1]) )


    return visited[n-1][n-1]


M = [
    [3,1,3,3,3],
    [3,1,3,1,3],
    [3,1,3,1,3],
    [3,3,3,1,3],
    [3,3,3,1,3],
]
print(to_port(M, 2))