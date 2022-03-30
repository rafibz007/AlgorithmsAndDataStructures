from random import randint, seed
from time import time

def counting_sort(A, k, f):
    C = [0]*k
    B = [0]*len(A)
    for i in range(len(A)): C[f(A[i])] += 1
    for i in range(1,k): C[i] += C[i-1]
    for i in range(len(A)-1, -1, -1):
        C[f(A[i])] -= 1
        B[C[f(A[i])]] = A[i]
    for i in range(len(A)): A[i] = B[i]

def number_len(number):
    counter = 0
    while number > 0:
        counter += 1
        number //= 10
    return counter

def radix_sort(A):
    for i in range(1,number_len(max(A))+1):
        counting_sort(A, 10, lambda x: ( int(x % (10**i) // ( 10**(i-1) ) ) ) )

def quicker_sort(T):
    def qsort(T, p, r):
        while p < r:
            q, t = partition(T, p, r)
            qsort(T, p, q-1)
            # print(T, p, q-1)
            p = t+1
        return T

    def partition(T, p, r):
        idx = randint(p, r)
        T[r], T[idx] = T[idx], T[r]

        pivot = T[r]
        t = 1
        i = p-1
        j = p
        while j < r-t+1:
            if T[j] == pivot:
                T[j], T[r-t] = T[r-t], T[j]
                t += 1
                j -= 1
            elif T[j] < pivot:
                i += 1
                T[i], T[j] = T[j], T[i]
            j += 1
        #after this loop 'j' will be at starting index of "pivots section"
        #'i' will be at the end of "lower section"


        y = i+1
        for x in range(j, r+1):
            T[y], T[x] = T[x], T[y]
            y += 1
        #at the end of lower section now is "pivots section"


        return i+1,i+t #return start_of_pivots end_of_pivots

    return qsort(T, 0, len(T)-1)


def bucket_sort_01(A):

    buckets = [ [] for _ in range( 10 ) ]

    for i in range(len(A)): buckets[ int(A[i]) ].append(A[i])
    for i in range( len(buckets) ): quicker_sort(buckets[i])

    a_index = 0
    for bucket in buckets:
        for i in range( len(bucket) ):
            A[a_index] = bucket[i]
            a_index += 1

def bucket_sort(A):
    min_val = A[0]
    max_val = A[-1]
    for i in range( len(A) ):
        if   A[i] < min_val: min_val = A[i]
        elif A[i] > max_val: max_val = A[i]

    buckets = [ [] for _ in range( (int(max_val)-int(min_val)+1) ) ]
    for i in range( len(A) ): buckets[ int((A[i]-min_val)) ].append(A[i])
    for i in range( len(buckets) ): quicker_sort( buckets[i] )
    a_index = 0
    print(len(buckets),buckets)
    for bucket in buckets:
        for i in range( len(bucket) ):
            A[a_index] = bucket[i]
            a_index += 1

def bucket_sort2(A):
    min_val = min(A)

    n = len(A)

    buckets = [ [] for _ in range(n) ]
    for i in range(len(A)): buckets[ int(A[i]-min_val) ].append(A[i])
    for i in range( len(buckets) ): quicker_sort( buckets[i] )
    a_index = 0
    # print(len(buckets),buckets)
    for bucket in buckets:
        for i in range( len(bucket) ):
            A[a_index] = bucket[i]
            a_index += 1

def bucket_sort3(A):
    n = len(A)
    min_val = min(A)
    max_val = max(A)
    rnge = (max_val-min_val)/n

    buckets = [ [] for _ in range(n) ]
    for i in range(len(A)):
        diff = (A[i] - min_val) / rnge - int((A[i] - min_val) / rnge)

        # append the boundary elements to the lower array
        if diff == 0 and A[i] != min_val:
            buckets[int((A[i] - min_val) / rnge) - 1].append(A[i])
        else:
            buckets[int((A[i] - min_val) / rnge)].append(A[i])

    a_index = 0
    for bucket in buckets:
        quicker_sort(bucket)
        for i in range(len(bucket)):
            A[a_index] = bucket[i]
            a_index += 1

    # print(buckets)

seed(42)

n = 100
T = [randint(0, 100)/(10**randint(1, 2)) for _ in range(n)]
# for i in range(1, len(T)): T[i] += T[i-1]
# T.append(0)
# TC = T[:]
# print(T)
start = time()
bucket_sort3(T)
end = time()
print(end-start)
# print(T)

# start = time()
# radix_sort(T)
# end = time()

# # print(T)
#
# start = time()
# quicker_sort(TC)
# end = time()
# print(end-start)
# # print(TC)

