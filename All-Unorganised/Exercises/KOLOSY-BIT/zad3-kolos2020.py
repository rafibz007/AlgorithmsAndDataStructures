

from random import randint, shuffle

def partition(A, p, r):
    idx = randint(p, r)
    A[r], A[idx] = A[idx], A[r]

    pivot = A[r]
    i = p - 1
    t = 1
    j = p
    while j < r-t+1:
        if A[j] < pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
        elif A[j] == pivot:
            A[r - t], A[j] = A[j], A[r - t]
            t += 1
            continue #aby sprawdzilo wymieniony element
        j += 1

    i += 1
    for x in range(t):
        A[i + x], A[r - x] = A[r - x], A[i + x]

    return i, i + t - 1 #return begin_of_pivot_section, end_of_...
def sort(A, p, r):
    if p<r:
        q, t = partition(A, p, r)
        sort(A, t+1, r)
        sort(A, p, q-1)
def is_sum_of_other_two(A, index):
    search = A[index]
    left = 0
    right = len(T)-1
    while left < right:
        sum = A[left]+A[right]
        if   search < sum: right -= 1
        elif search > sum: left += 1
        else: return True

        if   left == index: left += 1
        elif right == index: right -= 1
    return False

n = 10
T = [0, 0, 0, 1, 1, -1, -1, 2, 3, 5, 8, 13, 9]


sort(T, 0 , len(T)-1) #nlogn
every_number_is_sum = True
if len(T) < 3: every_number_is_sum = False
for i in range(len(T)): #n
    if not is_sum_of_other_two(T, i): #n
        every_number_is_sum = False
        break

#O(nlogn +n^2) = O(n^2)
print(every_number_is_sum)