"""

f(i,j) - najdluzszy wspolny podciag, liczony z i liter slowa A, oraz j liter slowa B

            | max( f(i-1, j), f(i,j-1) )                      A[i] != B[j]
f(i,j) =    |
            | max( f(i-1,j-1)+1, f(i-1, j), f(i,j-1) )        A[i] = B[j]

f( len(A), len(B) ) - rozwiazanie

"""

def max_subsequence(A,B):


    F = [ [0]+[None]*len(B) for _ in range(len(A)+1) ]
    F[0] = [0]*(len(B)+1)

    # for i in range(len(F)):
    #     print(F[i])


    for i in range(1,len(A)+1):
        for j in range(1,len(B)+1):

            if A[i-1] == B[j-1]:
                F[i][j] = max(F[i-1][j], F[i][j-1], F[i-1][j-1]+1)
            else:
                F[i][j] = max(F[i-1][j], F[i][j-1])

    # for i in range(len(F)):
    #     print(F[i])

    return F[len(A)][len(B)]


A = "alabama"
B = "aama"

print(max_subsequence(A,B))