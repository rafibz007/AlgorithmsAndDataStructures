# Wywolujac funkcje partirion i znajdujac dany piwot, sprawiamy ze wszywtkie mniejsze elementy beda po prawej, a mniesze po lewej
# Jezeli wiec selectem - zmodyfikowanym quick sortem - znajdziemy indeks poczatku jaki chcemy wyciac, to wszystkie wieksze elementy
# beda po prawej a mniejsze po lewej, jesli na prawej polowce ponownie wyszukamy 2 indeksu, to miedzy dwoma znalezionymi indeksami
# beda wszystkie wzrosty ktore powiny byc, ale nie uporzadkowane, wystarczy wywolac na tej czesci sorta ( chyba nie ze musza byc )
#
#  2*Select randomizowany - 2O(n)
#  1*sort na fragmencie - O(nlogn) -  w najgorszym przypadku
#  calkowita zlozonosc to wiec O(nlogn) jesli fragment musi bys uporzadkowany i O(n) jesli nie musi
#
# Algorytm dziala w miejscu, wiec zlozonosc pamieciowa to O(1)
#


from random import randint, shuffle

def partition(A, p, r):
    idx = randint(p, r)
    A[r], A[idx] = A[idx], A[r]

    pivot = A[r]
    i = p - 1
    t = 1
    j = p
    while j < r-t+1:
        if A[j] > pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
        elif A[j] == pivot:
            A[r - t], A[j] = A[j], A[r - t]
            t += 1
            continue #aby sprawdzilo wymieniony element
        j += 1

    i += 1
    for x in range(t):
        A[i + x], A[r - x] = A[r - x], A[i + x]

    return i, i + t - 1 #return begin_of_pivot_section, end_of_...

def select(A, p, r, k):
    if p == r: return
    q, t = partition(A, p, r)

    if   k < q: select(A, p, q-1, k)
    elif t < k: select(A, t+1, r, k)
    return

def section(T, p, q):
    select(T, 0, len(T)-1, p)
    select(T, p+1, len(T)-1, q)
    # sort(T, p, q) # <- to usunac aby nie sortowac fragmentu i otrzymac zlozonosc O(n)
    result = [ T[i] for i in range(p,q+1) ]
    return result

def sort(A, p, r):
    if p<r:
        q, t = partition(A, p, r)
        sort(A, t+1, r)
        sort(A, p, q-1)

n = 20
# T = [randint(-100, 100) for _ in range(n)]
T = list(range(n))
shuffle(T)
print(T)
A = section(T, 10, 19)
# sort(T,0, len(T)-1)
# for i in range(1,len(T)):
#     if T[i] > T[i-1]: print(i)
print(T, A, sep='\n')
