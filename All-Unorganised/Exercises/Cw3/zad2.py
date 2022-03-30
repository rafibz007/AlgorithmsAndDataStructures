def parent(i): return (i-1)//2


def push(T, n, v):
    T[n] = v
    i = n
    j = parent(i)
    # n += 1
    while i > 0 and T[j] < T[i]:
        T[j], T[i] = T[i], T[j]
        i = j
        j = parent(i)
