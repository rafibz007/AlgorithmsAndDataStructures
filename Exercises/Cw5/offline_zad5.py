# definiuje funkcje f(i) jako dlugosc najdluzszego przedluzanego podciagu zawartego w przedziale 0..i-1 przez liczbe int
# - tworze dla jej reprezentacji tablice F. Tablica S bedzie tablica przechowujaca moje potencjalne rozwiazania,
# bedzie ona zawierac indeksy poprzenich liczb, ktorych podciag przedluza i ktorych podciagi sa maksymalnej dlugosci do indeksu i.
# W ten sposob chcac odtworzyc rozwiazanie wystarczy rekurencyjnie wybierac kolejne indeksy w kazdym S[i].

#sortowanie przez zlicanie dla kolejnych indeksow tablicy
# lekko zmodyfikowana aby uniknac ciaglego kopiowania B do LS
# kopiuje tylko gdy skonczy sortowanie
def counting_sort(LS, B, n, f, k):

    C = [0]*n
    for i in range( len(LS) ): C[f(LS[i])] += 1
    for i in range( 1, n ): C[i] += C[i-1]
    for i in range( len(LS)-1, -1, -1 ):
        C[f(LS[i])] -= 1
        B[C[f(LS[i])]] = LS[i]

    if k == 0:
        for i in range( len(LS) ): LS[i] = B[i]
    else: counting_sort(B, LS, n, lambda x: x[k-1], k-1)


def radix_sort(A, LS):
    n = len(A)
    B = [0] * len(LS)
    k = len(LS[0])

    counting_sort(LS, B, n, lambda x: x[k-1], k-1)


def print_solutions(A, list_of_solutions):
    for solution in list_of_solutions:
        for i in range( len(solution) ):
            print(A[solution[i]], end=' ')
        print("")


#zwraca tablice tablic indeksow wszystkich rozwiazan, ktore koncza sie na danym indeksie
def solutions(S, index, solution, s_index ,list_of_solutions):

    # znaczy ze S[index] nie wskazuje juz na zaden kolejy element, wiec jest to koniec ciagu
    if len(S[index]) == 0:
        solution[s_index] = index

        # zapisuje otrzymane rozwiazanie aby pozniej je zwrocic
        list_of_solutions.append( solution[:] )
    else:
        #dla kazdego elementu S[index] wywoluje rekurencyjnie funkcje aby otrzymac wszystkie mozliwe rozwiazania
        for i in S[index]:
            solution[s_index] = index
            solutions(S, i, solution, s_index - 1, list_of_solutions)

    #zwracam liste rozwiazan
    return list_of_solutions

#zwraca tatblice tablic indeksow wszystkich rozwiazan
def get_solutions(F, S):
    n = len(F)
    max_len = max(F)
    list_of_solutions = []

    # w petli for szukam indeksow na ktorych konczy sie maksymalny podciag
    # jesli taki znajde wywoluje solutions, ktoro znajduje wszystkie podciagi maksymalnej dlugosci
    # konczace sie na danycm indeksie
    #robiac tak dla wszystkich maksymalnych indeksow odnajduje wszystkie wyniki
    for i in range(n):
        if F[i] == max_len:
            list_of_solutions += solutions(S, i, [-1]*max_len, max_len-1,[])

    #zwracam liste wynikow
    return list_of_solutions


def printALLLIS(A):
    n = len( A )

    F = [0]*n
    F[0] = 1

    S = [ [] for _ in range( n ) ]

    for i in range( 1, n ):
        q = 0
        for j in range( i ):

            # warunek spelniony jesli znaleziono lepszy lub rownej dlugosci podciag
            if A[j] < A[i] and q <= F[j]:

                # jesli ciag znaleziony jest lepszy, o poprzednich indeksach w S nalezy zapomniec, bo nie stworza juz rozwiazania
                if q < F[j]:
                    q = F[j]
                    S[i] = []

                # dodaje nastepny indeks ktory prowadzi do podciagu maksymalnej dlugosci w przedziale 0..i
                S[i].append( j )

        F[i] = q+1

    # otrzymuje liste list, zawierajcacyh kolejne indeksy kolejnych podciagow
    list_of_solutions = get_solutions(F, S)

    #sotuje po indeksach aby spelnic warunek wypisywania z tresci zadania
    radix_sort(A, list_of_solutions)

    #wypisuje podciagi w odpowiedniej juz kolejnosci
    print_solutions(A, list_of_solutions)
    return len(list_of_solutions)


# T = [ 10*k+1 for k in range(8) for i in range(6,0,-1) ]
T = [2, 1, 4, 3]
# T = [3,4,-1,5,8,2,3,12,7,9]
# print(len(T))

print(printALLLIS(T))
