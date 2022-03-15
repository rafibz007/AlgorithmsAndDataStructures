def bin_search(A, x):
    p = 0
    r = len(A)-1
    A.sort()

    while p <= r:
        q = int((p+r)/2)
        if A[q] > x: r = q-1
        elif A[q] < x: p = q+1
        else: return q

    return None


T = [ 0, 1, 1, 2, 2, 4, 5, 6, 7, 8, 9, 10, 12 ]
print(bin_search(T, 1))