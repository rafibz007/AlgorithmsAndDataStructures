def counting_sort(A, k = None, f = lambda x: x):
    if k is None: k = max(A)+1
    C = [0]*k
    B = [0]*len(A)
    for i in range(len(A)): C[f(A[i])] += 1
    for i in range(1,k): C[i] += C[i-1]
    for i in range(len(A)-1, -1, -1):
        C[f(A[i])] -= 1
        B[C[f(A[i])]] = A[i]
    for i in range(len(A)): A[i] = B[i]


def reverse_counting_sort(A, k = None, f = lambda x: x):
    if k is None: k = max(A)+1
    C = [0]*k
    B = [0]*len(A)
    for i in range(len(A)): C[f(A[i])] += 1
    for i in range(k-2,-1, -1): C[i] += C[i+1]
    for i in range(len(A)-1, -1, -1):
        C[f(A[i])] -= 1
        B[C[f(A[i])]] = A[i]
    for i in range(len(A)): A[i] = B[i]

T = [ 9, 1, 4, 56, 23, 5, 1, 0, 23, 12, 7 ]
counting_sort(T)
print(T)
T = [ 9, 1, 4, 56, 23, 5, 1, 0, 23, 12, 7 ]
reverse_counting_sort(T)
print(T)