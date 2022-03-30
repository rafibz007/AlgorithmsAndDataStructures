from random import randint, shuffle

def counting_sort(A, f):
    n = len(A)
    C = [0]*n
    B = [0]*len(A)
    for i in range(len(A)): C[f(A[i])] += 1
    for i in range(1,n): C[i] += C[i-1]
    for i in range(len(A)-1, -1, -1):
        C[f(A[i])] -= 1
        B[C[f(A[i])]] = A[i]
    for i in range(len(A)): A[i] = B[i]

def radix_sort(A):
    n = len(A)
    counting_sort(A, lambda x: x%n)
    counting_sort(A, lambda x: x//n)


n = 100
T = [ randint(0, n*n-1) for _ in range(n) ]
radix_sort(T)
for i in range(1,len(T)):
    if T[i] < T[i-1]: print(i)
print(T)