def insertion_sort(A):
    for i in range(1, len(A)):
        j = i
        curr = A[i]
        while j-1 >= 0 and A[j-1] > curr:
            A[j] = A[j-1]
            j -= 1
        A[j] = curr


def counting_sort(A, k):
    B = [0]*len(A)
    C = [0]*k
    for i in range(len(A)): C[A[i]] += 1
    for i in range(1,k): C[i] += C[i-1]
    for i in range(len(A)-1, -1, -1):
        C[A[i]] -= 1
        B[C[A[i]]] = A[i]
    for i in range(len(A)): A[i] = B[i]

def sort_10_diff(A, k):
    B = []
    C = []
    for i in range(len(A)):
        if 0 <= A[i] <= k: B.append(A[i])
        else: C.append(A[i])

    counting_sort(B, k)
    insertion_sort(C)

    b_index = 0
    c_index = 0
    for i in range(len(A)):
        if B[b_index] < C[c_index]:
            A[i] = B[b_index]
            b_index += 1
        else:
            A[i] = C[c_index]
            c_index += 1

