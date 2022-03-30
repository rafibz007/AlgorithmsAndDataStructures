def max_index(A):
    current_max = 0
    for i in range(len(A)):
        if A[i] > A[current_max]: current_max = i
    return current_max

def get_solution(A, S, i):
    if i < 0: return []
    if S[i] == -1: return [A[i]]
    return get_solution(A, S, S[i]) + [A[i]]

def findLIS(A):
    n = len(A)

    F = [0]*n
    F[0] = 1

    S = [-1]*n

    for i in range(1, n):
        q = 0
        for j in range(i):

            if A[j] < A[i] and q < F[j]:
                q = F[j]
                S[i] = j

        F[i] = q+1

    index = max_index(F)
    T = get_solution(A,S,index)
    return len(T), T


T = [13,7,21,42,8,2,44,53,1]
print(findLIS(T))


