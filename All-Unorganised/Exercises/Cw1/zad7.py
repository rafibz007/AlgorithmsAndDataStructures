#T - posortowana tablica
def find_sum(T, search_num):
    left = 0
    right = len(T)-1
    while left < right:
        current_sum = T[left] + T[right]
        if current_sum > search_num: right -= 1
        elif current_sum < search_num: left += 1
        else: return left,right
    #endWHILE
    return None

T = [2, 3, 6, 20, 28, 36, 58, 100, 1924, 2021]
print(find_sum(T, 128))
