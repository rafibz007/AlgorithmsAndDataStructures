# implementacja tspf jak na wykladzie, f(i,j) - najkrotsze drogi prowadzace 0 -> j, oraz z 0 <- i uzywajace
# wszystkich miast z przedzialu 0..(i)..j, przy zalozeniu i<j

# przy odtwarzaniu rozwiazania tworze 2 tablice S, R; jenda odpowiada za zapisywanie miast idac w prawo, druga w lewo
# dopoki i<j-1 znaczy to ze j nalezy do aktualnej drogi idacej w prawo, jesli cofajac sie natrafimy na i=j-1
# szukamy indeksu k ( 0 <= k < j-1 ) z ktorego wyglada ze skoczylismy aby dostac sie do indeksu j, a nastepie
# odwracamy problem teraz traktujemy jako dluzsza sciezke ta do indeksu i, cofajac sie i zapisujac wyniki w R
# nastepnie odpowiednio wszystko wypisuje zwracajac uwage na kolejnosc dodawania i wystepowania

from math import *


def partition( A, p, r, f ):
  pivot = f(A[r])
  i = p-1
  for j in range(p,r):
    if f(A[j]) < pivot:
      i += 1
      A[j], A[i] = A[i], A[j]

  i += 1
  A[i], A[r] = A[r], A[i]
  return i

def sort( A, p, r, f ):
  if p<r:
    q = partition(A, p, r, f)
    sort(A, p, q-1, f)
    sort(A, q+1, r, f)

def d( p1, p2 ):
  a = p1[1] - p2[1]
  b = p1[2] - p2[2]
  return ( a*a + b*b )**0.5



def get_solution( i, j, F, D, S, R ):

  if i < 0 or j < 0: return
  if i >= j: return

  #miasto na ktorym sie znajdujemy nalezy do drogi ktora sie przemieszczalismy wiec dodaje do tablicy
  S.append(j)

  if i < j-1:
    # skoro i<j-1 to miasto j-1 tez na pewno nalezy do aktualnej drogi
    get_solution( i, j-1, F, D, S, R )
  else:
    # i == j-1, wiec szukam miasta z ktorego skoczylismy do j, wywolujac nastepnie funkcje odwracajac problem
    # i szukajac teraz sciezki powrotnej do indeksu i, krotsza sciezka jest teraz do znalezionego indeksu skoku k
    k_found = -1
    for k in range( i ):
      if F[i][j] == F[k][i] + D[k][j]:
        k_found = k
        break
    #zamieniam tablice R,S, aby rozwiazania byly zapisywane do wlasciwej tablicy
    get_solution( k_found, i, F, D, R, S )

  #zwrocenie rozwiazan
  return S, R

#implementacja jak z wykladu
def tspf( i, j, F, D, inf ):

  if F[i][j] != inf or i >= j:
    return F[i][j]

  if i == j-1:
    best = inf

    for k in range( j-1 ):
      q =  tspf( k, j-1, F, D, inf ) + D[k][j]
      if q < best:
        best = q

    F[i][j] = best
  else:
    F[i][j] = tspf( i, j-1, F, D, inf ) + D[j-1][j]

  return F[i][j]


def bitonicTSP( C ):

  n = len(C)

  #sortowanie tablicy C po x
  sort( C, 0, n-1, lambda x: x[1] )

  #tworze tablice odleslosci, d(i,j) = D[i][j]
  D = [ [ d( C[i], C[j] ) for j in range(n) ] for i in range(n) ]

  #moja nieskonczonosc ktora wypelnie tablice F
  inf = 0
  for i in range(n): inf += sum(D[i])
  inf = inf//1 + 1

  #tablica rozwiazan rekurencyjnych
  F = [ [inf]*n for _ in range(n) ]

  F[0][1] = D[0][1]

  #wywolania funkcji i szukanie rozwiazania
  k_min = -1 # indeks i - czyli miasto z ktorego zaczynamy wracac - ktory dal najkrotsza droge
  best = inf
  for k in range( n-1 ):
    q = tspf( k, n-1, F, D, inf ) + D[k][n-1]
    if best > q:
      best = q
      k_min = k

  #odnalezienie i podanie rozwiazania
  S, R = get_solution( k_min, n-1, F, D, [], [] )

  print( C[0][0], end=" " )
  for i in range(len(S)): print( C[ S[-i-1] ][0], end=" " )
  for i in range(len(R)): print( C[ R[  i ] ][0], end=" " )
  print( C[0][0] )
  print(best)




C = [["Wrocław", 0, 2], ["Warszawa",4,3], ["Gdańsk", 2,4], ["Kraków",3,1]]

bitonicTSP( C )
