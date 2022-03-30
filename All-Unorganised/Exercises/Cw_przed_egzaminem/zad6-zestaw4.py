
def best_neigh(A):
    n = len(A)
    min_val = min(A)
    max_val = max(A)
    value_range = (max_val - min_val) / n

    buckets = [[] for _ in range(n)]
    for i in range(len(A)):
        ratio = (A[i] - min_val) / value_range
        diff = ratio - int(ratio)

        if diff == 0 and A[i] != min_val:
            buckets[int(ratio) - 1].append(A[i])
        else:
            buckets[int(ratio)].append(A[i])

    result = 0
    prev_max = max(buckets[0]) #na pewno nie bedzie puste
    for i in range(n):
        if len(buckets[i]) > 0:
            curr_min = min(buckets[i])
            result = max(result, curr_min-prev_max)
            prev_max = max(buckets[i])

    return result


A = [ 0, 0.5, 0.3, 0.01, 0.7, 0.2, 0.91, 0.11, 0.92, 1 ]
print(best_neigh(A))