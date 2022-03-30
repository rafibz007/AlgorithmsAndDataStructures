def left(i): return 2*i+1
def right(i): return 2*i+2
def parent(i): return int((i-1)/2)

#ZAIMPLEMENTOWANY JEST MAX HEAP, Z SORTOWANIEM ROSNACYM
def heapify( A, n, i ):
    m = i
    l = left(i)
    r = right(i)

    if l<n and A[m] < A[l]: m = l
    if r<n and A[m] < A[r]: m = r

    if m != i:
        A[m], A[i] = A[i], A[m]
        heapify(A, n, m)


def build_heap( A ):
    n = len(A)
    for i in range( parent(n-1), -1, -1 ):
        heapify(A, n, i)
    return A


def heap_sort( A ):
    build_heap(A)
    n = len(A)
    for i in range(n-1, 0, -1):
        A[0], A[i] = A[i], A[0]
        heapify(A, i, 0)
    return A


def push( A, n, value ):
    if n == len(A): A.append(0)
    A[n] = value
    j = n
    while j > 0 and A[parent(j)] < A[j]:
        A[parent(j)], A[j] = A[j], A[parent(j)]
        j = parent(j)
    return A

def pop( A, n ):
    A[n-1], A[0] = A[0], A[n-1]
    heapify(A, n-1, 0)
    return A[n-1]

T = [1,2, 3,5,6, 7,1, 5, 4, 1,1,2, 3,5,6, 7,1, 5, 4, 1,1,2, 3,5,6, 7,1, 5, 4, 1]

print(T)
print(build_heap(T))
print(T)
push(T, len(T), 100)
print(T)
# print(heap_sort(T))
# print(T)
print(pop(T, len(T)))
print(T)