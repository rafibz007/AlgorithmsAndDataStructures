from queue import Queue

class Node:
    def __init__(self, value=0):
        self.children = 0
        self.child = []
        self.value = value
        self.visited = False


def heavy_path(vertex):

    def bfs(vertex):
        queue = Queue()
        vertex.visited = True
        vertex.value = 0
        queue.put(vertex)

        max_vertex = vertex

        while not queue.empty():

            u = queue.get()
            for v, w in vertex.child:
                if not v.visited:
                    v.value = u.value + w

                    if v.value > max_vertex.value:
                        max_vertex = v

                    v.visited = True
                    queue.put(v)

        return max_vertex

    def dfs( vertex ):

        vertex.visited = False
        for v, _ in vertex.child:
            if v.visited:
                dfs(v)


    d1 = bfs(vertex)
    dfs(vertex)
    d2 = bfs(d1)
    return d2.value


if __name__ == '__main__':
    A = Node()
    B = Node()
    C = Node()
    A.children = 2
    A.child = [(B, 5), (C, -1)]
    B.child = [(A,5)]
    C.child = [(A, - 1)]
    print(heavy_path(A))