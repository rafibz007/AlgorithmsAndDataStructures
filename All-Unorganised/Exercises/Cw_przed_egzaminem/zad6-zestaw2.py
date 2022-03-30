"""
start_before - ilosc przedzialow zaczynajacych sie przed danym przzedzialem
end_before = ilosc przedzialow konczaca sie przed danym przzedzialem

Jesli jakis przedzial zaczyna sie przed danym przedzialem (w dowolnym miejscu) oraz konczy przed jego koncem,
to end_before - start_before da taki sam wynik jakby go nie bylo; end_before - start_before = end_before+1 - (start_before+1)

Jesli jakis przedzial zawiera sie w danym przedziale, to nie wliczy sie do start_before, ale wliczy do end_before,
zatem end_before-start_before za kazdy taki przedzial da 1

Jesli dany przedzial jest zawarty w jakims przedziale, to end_before - start_before zwroci bledny wynik, ale
to nie bedzie mialo znaczenia, bo ten przedzial i tak jest w czyms zawarty i znajdziemy na pewno lepsze rozwiazanie
"""


def quick_sort(A, I, f):

    def sort(p, r):
        if p < r:
            q = partition(p,r)
            sort(p,q-1)
            sort(q+1,r)

    def partition(p,r):
        nonlocal A, I, f

        pivot = f(A[I[r]])

        i = p-1
        for j in range(p,r):
            if f(A[I[j]]) <= pivot:
                i += 1
                I[j], I[i] = I[i], I[j]

        i += 1
        I[i], I[r] = I[r], I[i]
        return i

    sort(0, len(A)-1)


def intervals(A):

    n = len(A)
    I = [ i for i in range(n) ]

    start_before = [0]*n
    end_before = [0]*n

    quick_sort(A, I, lambda x: x[0])

    for i in range(1,n):
        if A[I[i]][0] == A[I[i-1]][0]:
            start_before[I[i]] = start_before[I[i-1]]
        else:
            start_before[I[i]] = start_before[I[i-1]]+1

    quick_sort(A, I, lambda x: x[1])
    for i in range(1,n):
        if A[I[i]][1] == A[I[i-1]][1]:
            end_before[I[i]] = end_before[I[i-1]]
        else:
            end_before[I[i]] = end_before[I[i-1]]+1


    amount_contain = [ end_before[I[i]]-start_before[I[i]] for i in range(n) ]

    max_idx = 0
    for i in range(n):
        if amount_contain[i] > amount_contain[max_idx]:
            max_idx = i

    return amount_contain[max_idx] if amount_contain[max_idx] else 0



A = [ [0,4], [5,7], [1,6], [3,5], [2,8] ]
print(intervals(A))