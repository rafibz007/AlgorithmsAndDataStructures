"""

f(i,s) - czy da sie osiagnac sume s, uzywajac pierwszych i elementow
f(i,s) = f(i-1,s) or f(i-1,s-A[i])
         nie biore        biore
         i-tego elem      i-ty elem

f(i,A[i]) = True

f(n,T) - odp

"""

def sum_to_T(A,T):

    def f(i,s):
        nonlocal F,A,T

        if i < 0 or s < 0: return False

        if F[i][s] is not None:
            return F[i][s]

        F[i][s] = f(i-1, s) or f(i-1, s-A[i])
        return F[i][s]

    def get_solution(i,s):
        nonlocal F,A,T, solution

        if s == A[i]:
            solution.append(A[i])
        elif i-1>=0 and s-A[i]>=0 and F[i-1][s-A[i]]:
            get_solution(i-1,s-A[i])
            solution.append(A[i])
        elif i-1>=0 and F[i-1][s]:
            get_solution(i-1,s)





    n = len(A)
    F = [ [None]*(T+1) for _ in range(n) ]

    for i in range(n):
        if A[i] <= T:
            F[i][A[i]] = True

    f(n-1,T)

    for i in range(n):
        print(F[i])

    solution = []
    get_solution(n-1,T)
    return f(n-1,T), solution if f(n-1,T) else []


A = [1,5,5,5,6]
print(sum_to_T(A,17))