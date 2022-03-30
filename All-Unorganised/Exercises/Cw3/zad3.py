from random import randint

def partition(T, p, r):
    i = p-1
    for j in range(p, r):
        if T[j] <= T[r]:
            i+=1
            T[j], T[i] = T[i], T[j]
    T[i+1], T[r] = T[r], T[i+1]
    return i+1

def quicksort(T):
    stack = []
    stack.append((0,len(T)-1))
    while len(stack) > 0:
        p, r = stack.pop()
        if p < r:
            q = partition(T, p, r)
            stack.append((p, q-1))
            stack.append((q+1, r))


n = 32
T = [ randint(10, 99) for _ in range(n) ]
print(T)
quicksort(T)
print(T)