def magic_fives( A ):
    def ceil(number):
        if number > number // 1:
            return int((number // 1) + 1)
        else:
            return int(number // 1)

    def sort_index_range(A, p, r):
        # sortuje tablice w przedziale indeksow p i r wlacznie
        for i in range(p + 1, r + 1):
            curr_number = A[i]
            j = i
            while j > p and A[j - 1] > curr_number:
                A[j] = A[j - 1]
                j -= 1
            A[j] = curr_number
        return A

    def rec_magic_fives(A, p, r):
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
        print(A)
        return rec_magic_fives(A, p, p+c-1)

    return rec_magic_fives(A, 0 ,len(A)-1)


T = [ 9, 1, 4, 56, 23, 5, 1, 0, -1, 23, -45, -2, 12, -5, 7 ]
print(magic_fives(T))
print(T)