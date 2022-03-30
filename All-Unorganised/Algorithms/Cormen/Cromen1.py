from random import randint

### DODAWANIE BINARNE

def dec_to_bin_tab(number, l=8):
    new_list = []
    while number > 0:
        new_list.insert(0, number%2)
        number //= 2
    #endWHILE
    while len(new_list) < l: new_list.insert(0, 0)
    return new_list

def bin_tab_to_dec(T):
    exp = 0
    dec_num = 0
    for idx in range(len(T)-1, -1, -1):
        dec_num += T[idx]*(2**exp)
        exp += 1
    return dec_num

def add_bin(A, B):
    C = [ 0 for _ in range( len(A)+1 ) ]
    carry = 0
    for index in range(len(A)-1, -1, -1):
        curr_sum = A[index]+B[index]+carry
        C[index+1] = curr_sum%2
        carry = curr_sum//2
    #endFOR
    C[0] = carry
    return C

###

### SORTOWANIA

def insertion_sort(T):
    for i in range(2, len(T)):
        current_number = T[i]
        j = i-1
        while j >= 0 and T[j] > current_number:
            T[j+1] = T[j]
            j -= 1
        T[j+1] = current_number
    return T

def selection_sort(T):
    for i in range(len(T)-1):
        idx_min = i
        for j in range(i, len(T)):
            if T[j] < T[idx_min]: idx_min = j
        T[idx_min], T[i] = T[i], T[idx_min]
    return T

def merge_sort(T):
    inf = max(T)+1
    def r_merge_sort(T, p, r):
        if p < r:
            q = (p+r)//2
            r_merge_sort(T, p, q)
            r_merge_sort(T, q+1, r)
            merge(T, p, q, r)

        return T

    def merge(T, p, q, r):
        nonlocal inf

        left_len = q-p+1
        right_len = r-q

        left = [0 for _ in range(left_len+1)]
        right = [0 for _ in range(right_len+1)]

        for i in range(left_len): left[i] = T[p+i]
        for i in range(right_len): right[i] = T[q+1 + i]

        left[left_len] = inf
        right[right_len] = inf

        i_left = 0
        j_right = 0
        for idx in range(p, r+1):
            # if i_left < left_len and j_right < right_len:
            if right[j_right] < left[i_left]:
                T[idx] = right[j_right]
                j_right += 1
            else:
                T[idx] = left[i_left]
                i_left += 1
            # elif i_left == left_len:
            #   T[idx] = right[j_right]
            #   j_right += 1
            # else:
            #   T[idx] = left[i_left]
            #   i_left += 1
            # WERSJA BEZ WAROWNIKA
            # NIE SPRAWDZANA
        return T

    return r_merge_sort(T, 0, len(T)-1)

#bez wartownikow w podlistach
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


#normal
def quick_sort1(T):

    def qsort(T, p, r):
        if p < r:
            q = partition(T, p, r)
            qsort(T, p, q)
            qsort(T, q + 1, r)

    def partition(T, p, r):
        pivot = T[r]
        i = p - 1
        for j in range(p, r):
            if T[j] <= pivot:
                i+=1
                T[j], T[i] = T[i], T[j]
        T[i+1], T[r] = T[r], T[i+1]
        return i+1



T = [1,3,0,2,4,7,-1]
print(T)
print(quick_sort1(T))
###

### WYSZUKIWANIE BINARNE, PODCIAGI I PODOBNE

def bin_search(T, search_num):
    # T = merge_sort(T)
    # T musi byc posortowana
    left = 0
    right = len(T)-1

    while left <= right:
        middle = (left+right)//2
        if T[middle] > search_num: right = middle-1
        elif T[middle] < search_num: left = middle+1
        else: return middle

    return None

def find_sum(T, x):
    # T = merge_sort(T)
    # T musi byc posortowane

    p = 0
    q = len(T)-1

    while p < q:
        if T[p] + T[q] < x: p += 1
        elif T[p] + T[q] > x: q -= 1
        else: return True

    return False

def count_inversions(A):
  counter = 0
  T = A.copy()

  def r_merge_sort(T, p, r):
    if p < r:
      q = (p + r) // 2
      r_merge_sort(T, p, q)
      r_merge_sort(T, q + 1, r)
      merge(T, p, q, r)

    return T

  def merge(T, p, q, r):
    nonlocal counter

    left_len = q - p + 1
    right_len = r - q

    left = [0 for _ in range(left_len)]
    right = [0 for _ in range(right_len)]

    for i in range(left_len): left[i] = T[p + i]
    for i in range(right_len): right[i] = T[q + 1 + i]

    i_left = 0
    j_right = 0
    idx = p
    while idx <= r and i_left < left_len and j_right < right_len:
        if right[j_right] < left[i_left]:
            T[idx] = right[j_right]
            j_right += 1
            counter += left_len-i_left
        else:
            T[idx] = left[i_left]
            i_left += 1
        idx += 1

    while idx <= r and i_left < left_len:
        T[idx] = left[i_left]
        i_left += 1
        idx += 1

    while idx <= r and j_right < right_len:
        T[idx] = right[j_right]
        j_right += 1
        idx += 1

    return T

  r_merge_sort(T, 0, len(T) - 1)
  return counter

def recursive_max_subarray(T):
    negative_inf = min(T)-1

    def crossed_subarray(T, left, mid, right):

        nonlocal negative_inf

        sum = 0
        left_sum = negative_inf
        max_left = mid
        for i in range(mid, left-1, -1):
            sum += T[i]
            if sum > left_sum:
                left_sum = sum
                max_left = i

        sum = 0
        right_sum = negative_inf
        max_right = mid + 1
        for i in range(mid+1, right+1):
            sum += T[i]
            if sum > right_sum:
                right_sum = sum
                max_right = i

        return max_left, max_right, right_sum+left_sum

    def subarray(T, left, right):
        if left == right:
            return left, right, T[left]

        mid = (left+right)//2

        low_left, low_right, low_sum = subarray(T, left, mid)
        high_left, high_right, high_sum = subarray(T, mid+1, right)
        cross_left, cross_right, cross_sum = crossed_subarray(T, left, mid, right)

        if low_sum > high_sum and low_sum > cross_sum: return low_left, low_right, low_sum
        elif high_sum > low_sum and high_sum > cross_sum: return high_left, low_right, high_sum
        else: return cross_left, cross_right, cross_sum

    return subarray(T, 0, len(T)-1)

def max_subarray(T):
    result = T[0]
    current_sum = 0
    for i in range(len(T)):
        current_sum += T[i]
        current_sum = max(0, current_sum)
        result = max(result, current_sum)
    return result

T = [1,3,-5,0,2,4,7,-1, 2]
print(recursive_max_subarray(T))
print(max_subarray(T))
print(T)
###