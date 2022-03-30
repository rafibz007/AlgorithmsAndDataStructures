def count_inversions(T):

    counter = 0

    def merge_sort(T, p, r):
        if p < r:
            q = (p+r)//2
            merge_sort(T, p, q)
            merge_sort(T, q+1, r)
            merge(T, p, q, r)

    def merge(T, p, q, r):
        nonlocal counter
        len_left = q-p+1
        len_right = r-q

        left = [T[p+i] for i in range(len_left)]
        right = [T[q+1+i] for i in range(len_right)]

        i_left = 0
        j_right = 0
        idx = p
        while i_left < len_right and j_right < len_right:
            if right[j_right] < left[i_left]:
                counter += len_left-i_left
                T[idx] = right[j_right]
                j_right += 1
            else:
                T[idx] = left[i_left]
                i_left += 1
            idx += 1

        while i_left < len_left:
            T[idx] = left[i_left]
            i_left += 1
            idx += 1

        while j_right < len_right:
            T[idx] = right[j_right]
            j_right += 1
            idx += 1

        return

    merge_sort(T, 0, len(T)-1)
    return counter

T = [0, 1, -1, 2, -2]
print(count_inversions(T))
print(T)