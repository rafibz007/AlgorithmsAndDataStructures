def quick_sort(A):

    def sort( p, r ):
        if p < r:
            q, t = partition(p, r)
            sort( p, q-1 )
            sort( t+1, r )


    def partition( p, r ):
        nonlocal A

        pivot = A[r]

        i = p-1
        t = 1
        j = p
        while j < r-t+1:
            if A[j] < pivot:
                i += 1
                A[i], A[j] = A[j], A[i]
            elif A[j] == pivot:
                t += 1
                A[j], A[r-t+1] = A[r-t+1], A[j]
                continue # aby sprawdzilo wymieniony element
            j += 1

        i += 1
        for idx in range( t ):
            A[i+idx], A[r-idx] = A[r-idx], A[i+idx]


        return i, i+t-1

    sort(0, len(A)-1)


def quick_sort2( A ):

    def sort( p, r ):
        nonlocal A
        if p < r:
            q = partition( p, r )
            sort(p, q-1)
            sort(q+1, r)

    def partition( p, r ):
        pivot = A[r]
        i = p-1
        for j in range( p, r ):
            if A[j] <= pivot:
                i += 1
                A[j], A[i] = A[i], A[j]

        i += 1
        A[i], A[r] = A[r], A[i]
        return i

    sort(0, len(A)-1)
    return A

T = [ 9, 1, 4, 56, 23, 5, 1, 0, -1, 23, -45, -2, 12, -5, 7 ]
quick_sort2(T)
print(T)