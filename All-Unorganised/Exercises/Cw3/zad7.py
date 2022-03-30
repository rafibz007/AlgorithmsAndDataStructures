from random import randint

def partition(T, p, r):
    pivot = T[p]
    i = p-1
    j = r+1
    while True:
        i+=1
        while T[i] < pivot: i += 1
        j-=1
        while T[j] > pivot: j -= 1
        if i < j: T[i], T[j] = T[j], T[i]
        else: return j

def rec_quick_sort(T, p, r):
    if p < r:
        q = partition(T, p, r)
        rec_quick_sort(T, p, q)
        rec_quick_sort(T, q+1, r)

n = 10
T = [ randint(10, 99) for _ in range(n) ]
print(T)
rec_quick_sort(T, 0, len(T)-1)
print(T)