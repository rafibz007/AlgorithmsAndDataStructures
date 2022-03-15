"""

f(i,g,d) - czy da sie ustawic i pierwszych samochodow, tak aby na gorze zostalo g miejsca, a na dole d miejsca

f(i,g,d) = f(i-1, g+A[i-1], d) or f(i-1, g, d+A[i-1])

"""

def cars(A,L):

    def get_solution(i,g,d):
        nonlocal F,A,L,S

        if g+A[i-1] <= L and F[i-1][g+A[i-1]][d]:
            S.append( [i-1, "g"] )
            get_solution(i-1, g+A[i-1], d)
        elif d+A[i-1] <= L and F[i-1][g][d+A[i-1]]:
            S.append( [i-1, "d"] )
            get_solution(i-1, g, d+A[i-1])

    def f(i,g,d):
        nonlocal F,A,L

        if g > L or d > L or i < 0: return False

        if F[i][g][d] is not None:
            return F[i][g][d]

        #pojawia sie A[i-1] bo indeksy sa przeskalowane o 1
        F[i][g][d] = f(i-1, g+A[i-1], d) or f(i-1, g, d+A[i-1])
        return F[i][g][d]


    n = len(A)
    F = [ [[None]*(L+1) for _ in range(L+1)] for _ in range(n+1) ]
    F[0][L][L] = True
    S = []

    for k in range(n, -1, -1):
        for i in range(n):
            for j in range(n):
                if f(k,i,j):
                    get_solution(k,i,j)
                    return k, S[::-1]


A = [ 1, 2, 3, 3, 7 ]
print(cars(A, 5))