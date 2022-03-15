from random import randint

def merge(t1, t2):
    merged = [ 0 for _ in range(len(t1)+len(t2))]

    i_t1 = 0
    j_t2 = 0
    idx = 0
    while i_t1 < len(t1) and j_t2 < len(t2):
        if t1[i_t1] < t2[j_t2]:
            merged[idx] = t1[i_t1]
            i_t1 += 1
        else:
            merged[idx] = t2[j_t2]
            j_t2 += 1
        idx += 1

    while i_t1< len(t1):
        merged[idx] = t1[i_t1]
        i_t1 += 1
        idx += 1

    while j_t2 < len(t2):
        merged[idx] = t2[j_t2]
        j_t2 += 1
        idx += 1

    return merged

def logn_merge(list_of_lists_to_merge, start, end):
    if end - start == 0: return list_of_lists_to_merge[start]
    if end - start == 1: return merge(list_of_lists_to_merge[start], list_of_lists_to_merge[end])

    q = (start+end)//2
    t1 = logn_merge(list_of_lists_to_merge, start, q)
    t2 = logn_merge(list_of_lists_to_merge, q+1, end)
    return merge(t1, t2)

n = 10
m = 10
T = [ [randint(-100, 100) for _ in range(randint(1, n))] for _ in range(m)]
sum_of_elem = 0
for i in range(len(T)):
    T[i].sort()
    sum_of_elem += len(T[i])
print(T)
print(sum_of_elem)
T_merged = logn_merge(T, 0, len(T)-1)
print(T_merged)
print(len(T_merged))