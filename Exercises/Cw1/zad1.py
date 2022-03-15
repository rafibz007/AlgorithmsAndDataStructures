def sort(T):
    for index in range(1, len(T)):
        current_element = T[index]
        i = index
        while i >= 1 and T[i-1] > current_element:
            T[i] = T[i-1]
            i -= 1
        #endWHILE
        T[i] = current_element
    return T

print(sort([5, 6, 3, 2, 6, 8, 0, 1, 9, 234, 567, 23, 46]))