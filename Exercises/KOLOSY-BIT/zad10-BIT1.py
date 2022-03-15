def amount_of_GCD(A):
    sqrt = int(len(A)**0.5)+1
    D = [[]]*sqrt #najwiekszy mozliwy dzielnik liczby
    for i in range(len(A)):
        for d in range(sqrt):
            if A[i] % d == 0:
                D[d].append(A[i])

    max_len = 0
    for i in range(1, sqrt):
        if len(D[max_len]) < len(D[i]): max_len = i

    return D[max_len]


