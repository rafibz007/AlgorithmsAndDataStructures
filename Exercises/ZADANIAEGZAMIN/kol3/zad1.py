

from inttree import *

# przykladowy test uzycia drzewa przedzialowego
# T = tree([1, 2, 3, 4, 5])
# tree_insert(T,(1, 4))
# tree_insert(T,(2, 5))
# tree_print(T)
# tree_remove(T,(1, 4))
# print()
# tree_print(T)
# tree_insert(T,(1, 3))
# print(tree_intersect(T, 3))
# exit(0)



def intervals( I ):
    n = len(I)

    A = []
    for i in range(n):
        A.append(I[i][0])
        A.append(I[i][1])

    A.sort()
    T = tree(A)
    tree_insert(T, [I[0][0], I[0][1]])

    res = [0 for _ in range(n)]
    res[0] = I[0][1] - I[0][0]

    #tree_print(T)

    for i in range(1, n): # O(n)
        interval = I[i]
        tree_insert(T, [I[i][0], I[i][1]]) # O(nlogn)
        flag = False
        for j in range(interval[0], interval[1] + 1): # O(n (logn + d)) , gdzie d to dlugosc najdluzszego przedzialu
            tmp = tree_intersect(T, j) # O( [n (logn + d)] * [k + logn] ), gdzie k to ilosc elementow w tmp
            if len(tmp) > 1:
                flag = True
                # print("OK")
                # print(tmp, j, i)

                max_val = -1
                min_val = float("inf")
                for elem in tmp:
                    max_val = max(max_val, elem[1])
                    min_val = min(min_val, elem[0])
                    tree_remove(T, elem) # O (n * (logn + d) * logn)
                    # tree_print(T)
                    # print(min_val, max_val)
                    # exit()
                tree_insert(T, [min_val, max_val]) # O( [n (logn + d)] * [k + logn] ), gdzie k to ilosc elementow w [min_val, max_val]

        if flag:
            # tree_insert(T, [min_val, max_val])
            new_val = max_val - min_val
        else:
            new_val = I[i][1] - I[i][0]

        res[i] = max(res[i - 1], new_val)


    # (1,3) , (4,9) , <- (3,5)
    # (4,9) <- (1,5)
    # (1, 9)

    return res



# uruchamia bazowe testy uzywajac funkcji intervals do obliczania wyniku
# wypisuje na koncu "OK!" jesli testy zaliczone
run_tests(intervals)





