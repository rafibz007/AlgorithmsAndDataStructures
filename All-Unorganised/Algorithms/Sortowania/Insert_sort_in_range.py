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