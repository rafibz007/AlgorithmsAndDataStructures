def select( A, k ):

    def rec_select( p, r ):
        nonlocal A, k
        if p == r: return A[p]

        q, t = partition(p,r)
        if k-1 <= q-1:
            return rec_select(p, q-1)
        if t+1 <= k-1:
            return rec_select(t+1, r)
        return A[q]

    def partition(p, r):
        nonlocal A

        pivot = A[r]

        i = p - 1
        t = 1
        j = p
        while j < r - t + 1:
            if A[j] < pivot:
                i += 1
                A[i], A[j] = A[j], A[i]
            elif A[j] == pivot:
                t += 1
                A[j], A[r - t + 1] = A[r - t + 1], A[j]
                continue  # aby sprawdzilo wymieniony element
            j += 1

        i += 1
        for idx in range(t):
            A[i + idx], A[r - idx] = A[r - idx], A[i + idx]

        return i, i + t - 1

    return rec_select(0, len(A)-1)

T = [ 9, 1, 4, 56, 23, 5, 1, 0, -1, 23, -45, -2, 12, -5, 7 ]
print(select(T, 11))
print(T)

