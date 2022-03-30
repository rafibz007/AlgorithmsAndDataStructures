"""

f(i,k) - minimalna liczba skokow jaka trzeba wykonac, aby dostac sie na i-te pole majac (po zjedzeniue przekaski
        z i-tego pola) dokladnie k energii

f(i,k) = min( f(i-j, k-A[i]+j)+1 | k-A[i]+j>=j ^ j nalezy do [1,i] )
f(0,A[i]) = 0
Gdy sie nie da, wartosc to inf
min(f(n-1, dowolne)) - odpowiedz

"""


def frog(A):

    def get_solution(i,k):
        nonlocal A,F,S
        # print(i,k)
        if i > 0:
            for j in range(1, i+1):
                if k-A[i]+j > 0:
                    if f(i,k) == f(i-j,k-A[i]+j)+1:
                        get_solution(i-j, k-A[i]+j)
                        break
        S.append(i)


    def f(i,k):
        nonlocal A,n,inf,F, max_energy
        if k <= 0 or k > max_energy: return inf
        # print(i,k)
        if F[i][k] > -inf:
            return F[i][k]

        F[i][k] = inf
        for j in range(1,i+1):
            if k-A[i] >= 0:
                F[i][k] = min( F[i][k], f(i-j, k-A[i]+j)+1 )

        return F[i][k]

    n = len(A)
    inf = float("inf")
    max_energy = sum(A)
    F = [ [-inf]*(max_energy+1) for _ in range(n) ]
    S = []
    # print(max_energy)
    F[0][A[0]] = 0

    best_energy = 0
    for k in range(max_energy+1):
        if f(n-1, best_energy) > f(n-1, k):
            best_energy = k

    get_solution(n-1, best_energy)

    return F[n-1][best_energy], S


A = [ 2, 1, 1, 1, 4, 2, 3, 1, 1, 1, 1, 1, 1 ]
print(frog(A))
A = [5, 2, 1, 8, 9, 1, 3, 2, 0]
print(frog(A))
