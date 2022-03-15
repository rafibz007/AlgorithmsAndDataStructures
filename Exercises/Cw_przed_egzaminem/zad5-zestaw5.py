"""

f(i,t) - maksymalny podzial przedzialu od 0 do i(wlacznie) na k przedzialow

f(i,t) = max( min(f(i-j, t-1), sum(A[i-j+1:j])) )
                i-j+1 >= t-1

f(i,1) = sum(A[0:i])

f(n-1,k) - rozwiazanie
"""

def minmax(A,k):

    def get_solution(i,t):
        nonlocal S,solution

        if t == 1:
            solution.append([0, i])
            return

        solution.append( [ S[i][t]+1, i ] )
        get_solution(S[i][t], t-1)

    def sum_idx_range(i,j):
        nonlocal A

        sum = 0
        for x in range(i,j+1):
            sum += A[x]
        return sum


    def f(i,t):
        nonlocal A, F, S

        if F[i][t] is not None:
            return F[i][t]

        best = -float("inf")
        for j in range(1,i):
            q = min( f(i-j, t-1), sum_idx_range(i-j+1, i) )
            if best < q:
                best = q
                S[i][t] = i-j

        F[i][t] = best
        return best


    n = len(A)
    F = [ [None]*(k+1) for _ in range(n) ]
    S = [[None] * (k + 1) for _ in range(n)]

    F[0][1] = A[0]
    for i in range(1,n):
        F[i][1] = F[i-1][1] + A[i]


    best = f(n-1, k)
    solution = []
    get_solution(n-1,k)


    return best, solution[::-1]




k = 3
#print(minmax(A, k))
A = [1, 5, 3, 8, 9, 10 ,11]
print(minmax(A, 3))

