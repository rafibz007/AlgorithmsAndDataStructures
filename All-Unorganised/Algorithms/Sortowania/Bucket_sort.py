
def partition(T, p, r):
    pivot = T[r]
    i = p-1
    for j in range(p, r):
        if T[j] <= pivot:
            i += 1
            T[j], T[i] = T[i], T[j]

    i += 1
    T[i], T[r] = T[r], T[i]
    return i

def quick_sort(T, p , r):
    if p<r:
        q = partition(T, p, r)
        quick_sort(T, q+1, r)
        quick_sort(T, p, q-1)


def bucket_sort(A):
    n = len(A)
    min_val = min(A)
    max_val = max(A)
    value_range = (max_val-min_val)/n

    buckets = [ [] for _ in range(n) ]
    for i in range(len(A)):
        ratio = (A[i] - min_val) / value_range
        diff = ratio - int(ratio)

        if diff == 0 and A[i] != min_val:
            buckets[int(ratio)-1].append(A[i])
        else:
            buckets[int(ratio)].append(A[i])
    a_index = 0
    for bucket in buckets:
        quick_sort(bucket, 0, len(bucket)-1)
        for i in range(len(bucket)):
            A[a_index] = bucket[i]
            a_index += 1


T = [ 9, 1, 4, 56, 23, 5, 1, 0, 23, 12, 7, -100, -23, 5 ]
bucket_sort(T)
print(T)