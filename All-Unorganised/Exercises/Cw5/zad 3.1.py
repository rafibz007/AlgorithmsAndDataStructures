def print_2d( A ):
    for i in range(len(A)):
        print(A[i])


def find( A, B ):
    a = len(A)+1
    b = len(B)+1

    F = [ [0]*b for _ in range(a) ]

    for i in range(1,a):
        for j in range(1,b):
            if A[i-1] == B[j-1]:
                F[i][j] = F[i-1][j-1]+1
            else:
                F[i][j] = max( F[i-1][j], F[i][j-1] )

    print_2d(F)
    return F[a-1][b-1]

A = [1, 7, 3, 2]
B = [7, 2, 4, 2, 3]

print(find(A, B))