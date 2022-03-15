def selection_sort( A ):
    for i in range(len(A)):

        min_idx = i
        for j in range( i, len(A) ):
            if A[j] < A[min_idx]: min_idx = j

        A[min_idx], A[i] = A[i], A[min_idx]


T = [ 9, 1, 4, 56, 23, 5, 1, 0, -1, 23, -45, -2, 12, -5, 7, -100 ]
selection_sort(T)
print(T)