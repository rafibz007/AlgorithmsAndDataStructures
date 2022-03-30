def left(i): return 2*i+1
def right(i): return 2*i+2
def parent(i): return (i-1)//2

def heapify(T, n, i): #tablica ilosc_elementow_kopca indeks_sprawdzanego_elementu
    l = left(i)
    r = right(i)
    m = i

    if l < n and T[m] < T[l]: m = l
    if r < n and T[m] < T[r]: m = r

    if m != i:
        T[m], T[i] = T[i], T[m]
        heapify(T, n, m)

def build_heap(T):
    n = len(T)
    for i in range(parent(n-1), -1, -1):
        heapify(T, n, i)
    return T

def heapsort(T):
    build_heap(T)
    n = len(T)
    for i in range(n-1, 0, -1):
        T[0], T[i] = T[i], T[0]
        heapify(T,i, 0)
    return T

def push(T, n, v):
    # T[n] = v
    T.append(v)
    i = len(T)-1 #i=n
    j = parent(i)
    while i > 0 and T[j] < T[i]:
        T[j], T[i] = T[i], T[j]
        i = j
        j = parent(i)
    return T

T = [1,2, 3,5,6, 7,1, 5, 4, 1,1,2, 3,5,6, 7,1, 5, 4, 1,1,2, 3,5,6, 7,1, 5, 4, 1]
# print(T)
print(build_heap(T))
print(T)
print(heapsort(T))
print(T)
# print(push(T, len(T), -1))