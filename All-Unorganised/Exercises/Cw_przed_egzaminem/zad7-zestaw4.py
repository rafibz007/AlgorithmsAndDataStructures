
def find_interval( A ):
    n = len(A)
    k = max(A)+1
    colors = [0]*k
    color_missing = 0

    i = 0
    j = 0
    colors[ A[i] ] += 1

    for l in range(k):
        while colors[l] == 0 and j+1<n:
            j += 1
            colors[ A[j] ] += 1

    best_ij = (i,j)
    best = j-i+1

    # print(i, j, colors)

    while j < n-1 or i < n-1:

        # print(i,j,n)

        while i+1<=j and colors[A[i]] != 1:
            colors[ A[i] ] -= 1
            i += 1
            if best > j - i + 1:
                best = j - i + 1
                best_ij = (i, j)

        colors[A[i]] -= 1
        if colors[A[i]] == 0: color_missing = A[i]
        i += 1

        while j+1<n and A[j+1] != color_missing:
            j += 1
            colors[A[j]] += 1

        if j+1<n:
            j += 1
            colors[A[j]] += 1

        # print(i, j, colors)
        if colors[color_missing] == 0: break



    return best, best_ij


A = [ 0, 1, 1, 2, 3, 3, 0, 0, 2, 2, 1, 1, 1, 1, 1, 0, 2, 3 ]
print(find_interval(A))