from random import randint, shuffle

def bin_search(A, value, f):
    if len(A) == 0: return -1

    left = 0
    right = len(A)-1
    while left <= right:
        mid = (left+right)//2
        if f(A[mid]) < value: left = mid+1
        elif value < f(A[mid]): right = mid-1
        else: return mid
    return -1


def insert(A, value, f):
    A.append(0)
    i = len(A)-1
    while i-1 >= 0 and f(A[i-1]) > value:
        A[i] = A[i-1]
        i -= 1
    A[i] = [value, 1]




def sort(A):
    uniq_values = []
    for i in range(len(A)):
        index = bin_search(uniq_values, A[i], lambda x: x[0])
        if index == -1: insert(uniq_values, A[i], lambda x: x[0])
        else: uniq_values[index][1] += 1
    # print(uniq_values)

    a_index = 0
    for uniq in uniq_values:
        for _ in range(uniq[1]):
            A[a_index] = uniq[0]
            a_index += 1



n = 10
k = 3
T = list(range(n))
T = T*3
# shuffle(T)
# print(bin_search(T, 9, lambda x: x))
print(T)
sort(T)
print(T)
# insert(T, -1, 3)
# print(T)