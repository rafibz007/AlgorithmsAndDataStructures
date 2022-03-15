from time import time


def counting_sort(LS, B, n, f, k):

    C = [0]*n
    for i in range( len(LS) ): C[f(LS[i])] += 1
    for i in range( 1, n ): C[i] += C[i-1]
    for i in range( len(LS)-1, -1, -1 ):
        C[f(LS[i])] -= 1
        B[C[f(LS[i])]] = LS[i]

    if k == 0:
        for i in range( len(LS) ): LS[i] = B[i]
    else: counting_sort(B, LS, n, lambda x: x[k-1], k-1)


def radix_sort(A, LS):
    n = len(A)
    B = [0] * len(LS)
    k = len(LS[0])

    counting_sort(LS, B, n, lambda x: x[k-1], k-1)


def print_solutions(A, list_of_solutions):
    for solution in list_of_solutions:
        for i in range( len(solution) ):
            print(A[solution[i]], end=' ')
        print("")


#zwraca tablice tablic indeksow wszystkich rozwiazan, ktore koncza sie na danym indeksie
def solutions(S, index, solution, s_index ,list_of_solutions):

    if len(S[index]) == 0:
        solution[s_index] = index
        list_of_solutions.append( solution[:] )
    else:
        for i in S[index]:
            solution[s_index] = index
            solutions(S, i, solution, s_index-1, list_of_solutions)

    return list_of_solutions

#zwraca tatblice tablic indeksow wszystkich rozwiazan
def get_solutions(F, S):
    n = len(F)
    max_len = max(F)
    list_of_solutions = []

    for i in range(n):
        if F[i] == max_len:
            list_of_solutions += solutions(S, i, [-1]*max_len, max_len-1,[])

    return list_of_solutions


def printALLLIS(A):
    n = len( A )

    F = [0]*n
    F[0] = 1

    S = [ [] for _ in range( n ) ]

    for i in range( 1, n ):

        q = 0
        for j in range( i ):

            if A[j] < A[i] and q <= F[j]:
                if q < F[j]:
                    q = F[j]
                    S[i] = []

                S[i].append( j )

        F[i] = q+1

    # print(F)
    # print(S)
    list_of_solutions = get_solutions(F, S)
    # print(list_of_solutions)
    radix_sort(A, list_of_solutions)
    # list_of_solutions.sort()

    # print(list_of_solutions)

    # print_solutions(A, list_of_solutions)
    return len(list_of_solutions)


T = [ 10*k+1 for k in range(8) for i in range(6,0,-1) ]
# T = [2, 1, 4, 3]
# print(len(T))

start = time()
print(printALLLIS(T))
end = time()

print(end-start)