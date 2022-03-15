def merge_sort( T ):

    def merge( p, q, r ):
        nonlocal T, W

        for i in range( p, r+1 ):
            W[i] = T[i]

        i = p
        j = q+1
        idx = p
        while i<q+1 and j<r+1:
            if W[j] < W[i]:
                T[idx] = W[j]
                j += 1
            else:
                T[idx] = W[i]
                i += 1
            idx += 1

        while i<q+1:
            T[idx] = W[i]
            i += 1
            idx += 1

        while j<r+1:
            T[idx] = W[j]
            j += 1
            idx += 1

        return

    def sort( p, r ):
        nonlocal T, W
        if p < r:
            q = (p + r) // 2
            sort( p, q )
            sort( q+1, r )
            merge( p,q,r )


    W = [ 0 ]*(len(T))
    sort(0, len(T)-1)
    return T

T = [ 9, 1, 4, 56, 23, 5, 1, 0, -1, 23, -45, -2, 12, -5, 7 ]
print(T)
merge_sort(T)
print(T)