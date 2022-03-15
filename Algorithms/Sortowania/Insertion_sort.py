def insertion_sort( A ):
    for i in range( 1, len(A) ):
        j = i
        x = A[i]
        while j-1 >= 0 and A[j-1] > x:
            A[j] = A[j-1]
            j -= 1
        A[j] = x


T = [ 9, 1, 4, 56, 23, 5, 1, 0, -1, 23, -45, -2, 12, -5, 7, -100 ]
insertion_sort(T)
print(T)