# Liniowo przechodze po tablicy zmieniajac ja na tablice krotek (pierwotna_liczba, ilosc_jednokrotnych, ilosc_dwukrotnych),
# nastepnie dwukrotnie wywoluje funkcje counting sort, sortujac najpierw po ilosci dwukrotnych(bo sa mniej istotne), a nastepnie
# po ilosci jednokrotnych - O(2n), na koniec wracam tablicy tylko jej pierwotne wartosci
# funkcja liczaca ilosc jednokrotnych i dwukrotnych przechodzi liniowo po cyfrze O(d), gdzie d - ilosc cyfr, wywolana bedzie n razy
# wiec O(dn)

# Calkowita zlozonosc bedzie wiec wynosic O(dn) + O(2n) + O(n) = O(dn), przt zalozeniu, ze d <<< n otrzymujemy O(n)
# Zlozonosc pamieciowa wynosci bedzie O(6n) - czyli O(n), bo na kazdy element tablic trzeba bedzie utworzyc krotke 3x dluzsza,
# oraz przy kazdym wywolaniu counting sorta trzeba bedzie utworzyc kopie tej tablicy

from random import shuffle

def amount_of_once_n_multi(number):
    tab_number = [0]*10
    if number == 0: tab_number[0] += 1
    while number > 0:
        tab_number[ number % 10 ] += 1
        number //= 10

    count_once = 0
    count_multi = 0
    for i in range(10):
        if   tab_number[i] == 1: count_once += 1
        elif tab_number[i] > 1: count_multi += 1

    return count_once, count_multi

def counting_sort(T, f):
    k = 11
    C = [0]*k  #bo mozliwe 11 wartosci, moze wystapic od 0 do 10 liczb jednokrotnych
    B = [0]*len(T)
    for i in range(len(T)): C[f(T[i])] += 1
    for i in range(1,k): C[i] += C[i-1]
    for i in range(len(T)-1, -1, -1):
        C[f(T[i])] -= 1
        B[C[f(T[i])]] = T[i]
    for i in range(len(T)): T[i] = B[i]

def reverse_counting_sort(T, f):
    k = 11
    C = [0]*k  #bo mozliwe 11 wartosci, moze wystapic od 0 do 10 liczb jednokrotnych
    B = [0]*len(T)
    for i in range(len(T)): C[f(T[i])] += 1
    for i in range(k-2, -1, -1): C[i] += C[i+1]
    for i in range(len(T)-1, -1, -1):
        C[f(T[i])] -= 1
        B[C[f(T[i])]] = T[i]
    for i in range(len(T)): T[i] = B[i]


def pretty_sort(T):
    for i in range(len(T)):
        once, multi = amount_of_once_n_multi(T[i])
        T[i] = (T[i], once, multi)

    # liczby wielokrotne trzeba posortowac najpierw w kolejnosci rosnacej
    counting_sort(T, lambda x: x[2])

    #liczby jednokrotne w kolejnosci malejacej
    reverse_counting_sort(T, lambda x: x[1])


    for i in range(len(T)):
        T[i] = T[i][0]



T = [123, 455, 1266, 114577, 2344, 67333, 0]
for _ in range(10):
    shuffle(T)
    pretty_sort(T)
    print(T)

