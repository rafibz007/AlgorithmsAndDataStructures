def find_sum(T, search_sum):
    left = 0
    right = len(T)-1

    while left < right:
        curr_sum = T[left]+T[right]
        if search_sum > curr_sum: left += 1
        elif search_sum < curr_sum: right -= 1
        else: return left, right

    return -1

T = [1, 2, 3,5, 6,7 ,8, 9, 10]
print(find_sum(T, 5))

def bin_search(T, search_num):
    left = 0
    right = len(T)-1
    while left <= right:
        mid = (left+right)//2
        if T[mid] < search_num: left = mid+1
        elif T[mid] > search_num: right = mid-1
        else: return mid
    return -1

print(bin_search(T, 4))