from random import randint

def quicker_sort(T):
    def partition(T, p, r):
        pivot = T[r]
        t = 1
        i = p-1
        j = p
        while j < r-t+1:
            if T[j] < pivot:
                i+=1
                T[i], T[j] = T[j], T[i]
            elif T[j] == pivot:
                T[r-t], T[j] = T[j], T[r-t]
                j -= 1
                t += 1
            j += 1

        i += 1
        for idx in range(t):
            T[i+idx], T[r-idx] = T[r-idx], T[i+idx]

        return i, i+t-1 #return begin_of_pivots, end_of_pivots

    def rec_quicker_sort(T, p, r):
        while p<r:
            q1, q2 = partition(T, p, r)
            # print(q1,q2,T[q1], T[q2],T)
            if q1-p-1 < r-q2:
                rec_quicker_sort(T, p, q1-1)
                p = q2 + 1
            else:
                rec_quicker_sort(T, q2+1, r)
                r = q1 - 1
        return T

    return rec_quicker_sort(T, 0, len(T)-1)

n = 2**16
T = [randint(1, 16) for _ in range(n)]
print(T)
print("START")
quicker_sort(T)
print("STOP")
print(T)
# T.append(0)
for i in range(1, len(T)):
    if T[i-1] > T[i]:
        print("NO")
        exit(0)