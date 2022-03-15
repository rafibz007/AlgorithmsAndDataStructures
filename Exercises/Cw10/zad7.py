# Odleglosc w kazdym wierzcholku przechowuje w postaci krotki
# ( <min cena gdy zostalo 0 paliwa>, <1 paliwa>, <2 paliwa>, ... , <D paliwa> )  gdzie D - pojemnosc baku
#
# Oraz jego parentow dla kazdego paliwa
# ( <parent przy 0 paliwa>, <1 paliwa>, <2 paliwa>, ... , <D paliwa> )
#
# Uzywac bede algorytmu dijkstry wrzucajac do kopca krotki
# ( <min koszt>, <pozostale paliwo po wjechaniu do wierzcholka>, <docelowy wierzcholek> )
#
# Gdy wjezdzamy do wierzcholka na ktorym jest stacja to mozemy dotankowac do kazdej ilosci paliwa powyzej tej ktora nam pozostala
# wrzucamy wtedy do kolejki wiele krotek (jedziemy z u do v) jesli da sie zrelaksowac ( wzor nizej )
# ( <min koszt>+k*c, <pozostale paliwo> - G[u][v]+k, v )
# gdzie k - litry ktore tankujemy, c - cena na danej stacji
#
# Przy wyciagnieciu wierzcholka u i przegladaniu jego sasiadow, np wierzcholka v, dokonujemy relaksacji wtw, gdy
# d[v][<pozostale paliwo> - G[u][v]] > d[u][<pozostale paliwo>] i wtedy dorzucamy do kolejki krotke
# ( d[u][<pozostale paliwo>], <pozostale paliwo> - G[u][v], v )
#
# Przy kazdej takiej relaksjacji aktualizuje rodzica na wierzcholek z ktorego przyjechalem
#
# wynik i sciezkie da sie latwo odtworzyc i odczytac z danego wierzcholka t

