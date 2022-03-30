from random import randint, seed

def partition(T, p, r):
    idx = randint(p,r)
    T[r], T[idx] = T[idx], T[r]

    pivot = T[r]
    i = p-1
    for j in range(p, r):
        if T[j] <= pivot:
            i+=1
            T[j], T[i] = T[i], T[j]
    T[i+1], T[r] = T[r], T[i+1]
    return i+1

def rec_find_k_smallest_value(T, p, r, k):
    if p < r:
        q = partition(T, p, r)
        if q > k-1: return rec_find_k_smallest_value(T, p, q - 1, k)
        if q < k-1: return rec_find_k_smallest_value(T, q + 1, r, k)
        return T[q]
    else: return T[p] #because p==r and it is an index of our found element


def find_k_smallest_value(T, k):
    if k < 1: return
    else: return rec_find_k_smallest_value(T, 0, len(T)-1, k)

# seed(42)

n = 10
# k = 5
for k in range(1,n+1):
    for _ in range(10):
        T = [randint(-100, 100) for _ in range(n)]
        k_smallest1 = find_k_smallest_value(T,k)
        T.sort()
        k_smallest2 = T[k-1]
        if not k_smallest1 == k_smallest2: print("NO")

