from math import log2, ceil

"""
bin_search: x(nalezace do A) -> [0, log2n](indeks)
C: i(indeks) -> amount(ilosc danego elementu)

obie funkcje sa bijekcjami, zatem kazdy x w czasie loglogn zostaje jednoznacznie zamieniony na
ilosc jego wystapien w tablicy A

na tej zasadzie uzywam counting sorta
"""


def weird_sort(A):

    def insert(value):
        nonlocal B, b_len

        j = b_len
        while j-1>=0 and B[j-1] > value:
            B[j] = B[j-1]
            j -= 1

        B[j] = value
        b_len += 1


    def bin_search(value):
        nonlocal B ,b_len

        p = 0
        r = b_len-1

        while p <= r:
            q = int( (p+r)/2 )

            if B[q] > value: r = q-1
            elif B[q] < value: p = q+1
            else: return q

        return None


    n = len(A)
    B = [float("inf")]*ceil(log2(n))
    T = [0]*n
    b_len = 0

    for i in range(n):
        if bin_search(A[i]) is None:
            insert(A[i])

    C = [0]*b_len
    for i in range(n): C[ bin_search(A[i]) ] += 1
    for i in range(1,ceil(log2(n))): C[i] += C[i-1]
    for i in range(n-1, -1, -1):
        C[ bin_search(A[i]) ] -= 1
        T[C[ bin_search(A[i]) ]] = A[i]
    for i in range(n): A[i] = T[i]





from random import randint, shuffle

lg2 = 3
A = [randint(0,10)]
for i in range(1,lg2):
    A.append( A[i-1]+randint(1,10) )

n = 2**lg2

for i in range(n-lg2):
    A.append( A[randint(0,lg2-1)] )

shuffle(A)
print(A)
weird_sort(A)
print(A)

