from random import randint
class Node:
    def __init__(self):
        self.value = None
        self.next = None


def ceil(number):
  if number > number//1:
    return int((number//1)+1)
  else: return int(number//1)

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

def max_subarray(T):
    result = T[0]
    current_sum = 0
    for i in range(len(T)):
        current_sum += T[i]
        current_sum = max(0, current_sum)
        result = max(result, current_sum)
    return result

def magic_fives(A, p, r):
  if p == r: return A[p]

  #ilosc moich median
  c = ceil((r-p+1)/5)

  for i in range(c):
    #krance danego przedzialu, ktorego szukam mediany
    begin = 5*i+p
    end = begin+4
    end = min(end, r)

    #sortuje dany przedzial dlugosci 5 lub mniejszej
    sort_index_range(A, begin, end)
    #mediana bedzie znajdowac sie na jego srodku(gdy dl. 5) - przeciwnym razie gdy dl. parzysta biore mniajsza z median
    median_index = (begin+end)//2

    #zamienianie median, aby znajdowaly sie na pocztku wszystkich przedzialow w tym wywolaniu magic_fives
    A[p+i], A[median_index] = A[median_index], A[p+i]

  #wywolanie funkcji na nowo powstalym przedziale median, aby znalezc ich mediane
  return magic_fives(A, p, p+c-1)

def linearselect( A, k ):

  def partition(A, p, r):
    #podzial tablicy na sekcje mniejsz od pivota/wieksze of pivota/rowne pivotowi

    # funkcja magic_fives ustawi pivot na pozycje A[p], ale w mojej implementacji w sumie to bez znaczenia
    pivot = magic_fives(A, p, r)
    t = 0
    i = p - 1
    j = p
    while j < r - t + 1:
      if A[j] < pivot:
        i += 1
        A[i], A[j] = A[j], A[i]
      elif A[j] == pivot:
        A[r - t], A[j] = A[j], A[r - t]
        j -= 1
        t += 1
      j += 1

    #przestawienie tablicy aby ulozona byla nastepujaco: mniejsz od pivota/rowne pivotowi/wieksze of pivota
    i += 1
    for idx in range(t):
      A[i + idx], A[r - idx] = A[r - idx], A[i + idx]

    return i, i+t-1  # return begin_of_pivots, end_of_pivots

  #rekurencyjny select
  def rec_lin_select(A, p, r, k):
    if p == r: return A[p]

    # po wywolaniu tego elementy od q1 do q2 beda juz na swoich indeksach jakby byly posortowane
    q1, q2 = partition(A, p, r)

    #szukany indeks jest na prawo od znalezionego pivota
    if k > q2: return rec_lin_select(A, q2+1, r, k)
    # szukany indeks jest na lewo od znalezionego pivota
    if k < q1: return rec_lin_select(A, p, q1-1, k)
    # szukany indeks jest rowny pivotowi
    return A[k]


  return rec_lin_select(A, 0, len(A)-1, k)

def max_subarray(T):
    result = T[0]
    current_sum = 0
    for i in range(len(T)):
        current_sum += T[i]
        current_sum = max(0, current_sum)
        result = max(result, current_sum)
    return result

