"""

f(i) - maksymalny zysk jaki mozna uzyskac do pola i

f(i) = max( f(i-1), f(i-2)+A[i] )

"""


def cut_forest(A):

    def get_solution(i):
        nonlocal A,F,solution

        if i < 2:
            if F[2] == F[0]+A[0]:
                solution.append(0)
            else:
                solution.append(1)
        else:

            if F[i] == F[i-2]+A[i]:
                solution.append(i)
                get_solution(i-2)
            else:
                get_solution(i-1)



    n = len(A)
    inf = float("inf")
    F = [-inf]*n

    F[0] = max(A[0], 0)
    F[1] = max(A[0],A[1], 0)


    for i in range(2, n):
        F[i] = max( F[i-1], F[i-2]+A[i] )

    best = F[n-1]
    solution = []
    get_solution(n-1)
    return best, solution[::-1]



C = [2, 4, 5, 100, 15, 4, 12]
print(cut_forest(C))