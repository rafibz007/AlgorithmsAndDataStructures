"""

f(i) - maksymalna ilosc klosckow, ktore ustawione beda poprawnie po usunieciu reszty, konczaca sie na klocku i-tym

f(i) = max( f(j)+1 | klocek i miesci sie w klocku j ^ j<i )

"""

def blocks(S):

    def contains(A,B):
        return A[0] <= B[0] and B[1] <= A[1]

    def get_solution(i):
        nonlocal R, solution

        solution.append(i)
        if R[i] == -1: return
        get_solution(R[i])


    n = len(S)
    inf = float("inf")
    F = [1]*n
    R = [-1]*n

    for i in range(n):
        for j in range(i):
            if contains(S[j], S[i]):
                q = F[j]+1
                if F[i] < q:
                    F[i] = q
                    R[i] = j


    print(contains( [-100,100], [1,2] ))
    solution = []

    best_idx = 0
    for i in range(1,n):
        if F[i] > best_idx:
            best_idx = i

    get_solution(best_idx)

    real_solution = [ i for i in range(n) if i not in solution ]

    return n-F[best_idx], real_solution


S = [ [-1, 3], [0, 5], [1, 11], [2, 4], [2, 9], [5, 8], [6, 7] ]
print(blocks(S))