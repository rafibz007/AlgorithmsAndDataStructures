from random import randint
class Node:
    def __init__(self):
        self.value = None
        self.next = None


def insertion_sort(T):
    for i in range(2, len(T)):
        current_number = T[i]
        j = i-1
        while j >= 0 and T[j] > current_number:
            T[j+1] = T[j]
            j -= 1
        T[j+1] = current_number
    return T

def insertion_sort2(T, f):
    for i in range(1, len(T)):
        j = i
        x = T[i]
        while j-1 >= 0 and f(T[j-1]) > f(x):
            T[j] = T[j-1]
            j -= 1
        T[j] = x

def selection_sort(T):
    for i in range(len(T)-1):
        idx_min = i
        for j in range(i, len(T)):
            if T[j] < T[idx_min]: idx_min = j
        T[idx_min], T[i] = T[i], T[idx_min]
    return T

def merge_sort2(T):

    def merge_sort(T, start, end):
        if start < end:
            mid = (start+end)//2
            merge_sort(T, start, mid)
            merge_sort(T, mid+1, end)
            merge(T, start, mid,end)

        return T

    def merge(T, start, mid, end):
        len_left = mid-start+1
        len_right = end-mid

        left = [0 for _ in range(len_left)]
        right = [0 for _ in range(len_right)]

        for i in range(len_left): left[i] = T[start+i]
        for i in range(len_right): right[i] = T[mid+1+i]

        index = start
        i_left = 0
        j_right = 0
        while i_left < len_left and j_right < len_right:
            if right[j_right] < left[i_left]:
                T[index] = right[j_right]
                j_right += 1
            else:
                T[index] = left[i_left]
                i_left += 1
            index += 1

        while i_left < len_left:
            T[index] = left[i_left]
            i_left += 1
            index += 1

        while j_right < len_right:
            T[index] = right[j_right]
            j_right += 1
            index += 1

        return T

    return merge_sort(T, 0, len(T)-1)

def counting_sort(A, k, f):
    C = [0]*k
    B = [0]*len(A)
    for i in range(len(A)): C[f(A[i])] += 1
    for i in range(1,k): C[i] += C[i-1]
    for i in range(len(A)-1, -1, -1):
        C[f(A[i])] -= 1
        B[C[f(A[i])]] = A[i]
    for i in range(len(A)): A[i] = B[i]

def reverse_counting_sort(A, k, f):
    C = [0]*k
    B = [0]*len(A)
    for i in range(len(A)): C[f(A[i])] += 1
    for i in range(k-2,-1, -1): C[i] += C[i+1]
    for i in range(len(A)-1, -1, -1):
        C[f(A[i])] -= 1
        B[C[f(A[i])]] = A[i]
    for i in range(len(A)): A[i] = B[i]

def sort_index_range(A, p, r):
  #sortuje tablice w przedziale indeksow p i r wlacznie
  for i in range(p+1, r+1):
    curr_number = A[i]
    j = i
    while j > p and A[j-1] > curr_number:
      A[j] = A[j-1]
      j -= 1
    A[j] = curr_number
  return A

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

#bedzie miala wartownika - lista
def selection_sort_list(head):
    new_head = Node()
    new_pointer = new_head
    while head.next is not None:
        pointer = head.next
        prev = head
        min_pointer = pointer
        min_prev = prev
        while pointer is not None:
            if min_pointer.value > pointer.value:
                min_pointer = pointer
                min_prev = prev
            prev = pointer
            pointer = pointer.next
        new_pointer.next = min_pointer
        new_pointer = new_pointer.next
        min_prev.next = min_pointer.next
    return new_head