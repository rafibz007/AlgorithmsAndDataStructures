"""
liczby z przedzialu n^2-1 mozna zapisac jako liczby o podstawie n:
    n^2 - 1 = (n-1)*n + (n-1)*1

    Jesli wiec posortuje je w podstawie n, beda posortowane w podstawie 10

Uzywam radix sorta

"""

def counting_sort(A,k,f):
    n = len(A)
    C = [0]*k
    B = [0]*n
    for i in range(n): C[f(A[i])] += 1
    for i in range(1, k): C[i] += C[i-1]
    for i in range(n-1, -1, -1):
        C[f(A[i])] -= 1
        B[C[f(A[i])]] = A[i]

    for i in range(n): A[i] = B[i]


def radix_sort(A, n):
    counting_sort(A,n, lambda x: x%n)
    # print(A)
    counting_sort(A,n, lambda x: x//n)
    # print(A)



from random import randint

n = 10
A = [ randint(0, n**2-1) for _ in range( randint(30, 100) ) ]
print(A)
radix_sort(A,n)
print(A)
for i in range(1,len(A)):
    if A[i-1] > A[i]:
        print(f"Err at index {i}:  {A[i-1]} > {A[i]}")