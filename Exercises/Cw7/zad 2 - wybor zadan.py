def partirion( A, B, p, r ):
    pivot = A[r]
    i = p-1
    for j in range( p, r ):
        if A[j] > pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
            B[i], B[j] = B[j], B[i]

    i += 1
    A[i], A[r] = A[r], A[i]
    B[i], B[r] = B[r], B[i]
    return i

def qsort( A, B, p, r ):
    if p < r:
        q = partirion( A, B, p, r )
        qsort( A, B, p, q-1 )
        qsort( A, B, q+1, r )

# w chwili t moge wykonac tylko zadania o terminie t+1, wiec wybieram najlepsze z nich
# w chwili t-1 tylko o terminie t+1 i t, wiec wybieram najlepsze z nich. itd
# implementacyjnie po kazdym wyborze zmniejszam nie wybraym termino jeden a wybrane przenosze na poczatek
def max_val( D, G ):
    n = len(G)
    qsort( D, G, 0, n-1 )

    time = D[0]
    S = [-1]*time
    for t in range( time-1, -1, -1 ):
        found_tasks = n-t-2
        i = found_tasks
        current_max = i

        while i<n and D[i]==t+1:

            if G[i] > G[current_max]:
                current_max = i

            D[i] -= 1
            i += 1

        S[t] = G[current_max]
        #przenosze znalozione juz taski na poczatek listy aby znowu ich nie szukac
        G[current_max], G[found_tasks] = G[found_tasks], G[current_max]
        D[current_max], D[found_tasks] = D[found_tasks], D[current_max]

    return sum(S), S




D = [5,4,4,3,1,2]
G = [8,7,5,4,4,2]

print(max_val(D, G))
# print(D)
# print(G)