def get_min_and_max(T):
    min_val = T[0]
    max_val = T[0]
    i = len(T)%2
    while i < len(T):
        if T[i] < T[i+1]:
            if T[i] < min_val: min_val = T[i]
            if T[i+1] > max_val: max_val = T[i+1]
        else:
            if T[i+1] < min_val: min_val = T[i+1]
            if T[i] > max_val: max_val = T[i]
        #endIF
        i+=2
    #endWHILE
    return min_val, max_val


print(get_min_and_max([2,4,345,235,1,3,6,5,23,7,52,35,58,1,-50, 0]))
