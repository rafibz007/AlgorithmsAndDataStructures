#zakladam ze tablica T jest posortowana
def find_index(T, x):
    left = 0
    right = len(T)-1

    while left <= right:
        mid = (left+right)//2
        print(T[mid])
        if T[mid] > x: right = mid-1
        elif T[mid] < x: left = mid+1
        else:
            while mid >= 1 and T[mid-1] == x: mid -= 1
            return mid
    #endWHILE
    return None
T = [1,1,1,1,1,1,1,1,3,3,3,456,45,45,45,345,2,4235,4,676,87,9,70,3]
print(find_index(T, 1))
print(len(T))