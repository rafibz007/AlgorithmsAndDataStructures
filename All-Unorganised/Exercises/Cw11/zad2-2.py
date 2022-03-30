"""
Aby trasa wyscigu byla poprawna, nie moze byc skrzyzowac, do kazdego miasta trzeba wiec wjechac i wyjechac jedna autostrada
Jesli wiec do wierzcholka a wchodza krawedzie x i y, a wychodza krawedziep p i q, to interpretuje to jako wartosc logiczna
czyli ( x xor y ) and ( p xor q ) - znaczy, ze wjedziemy jedna autostrada, a wyjedziemy tez jedna
po przeksztalceniach takie wyrazenie daje: (x=>~y) and (y=>~x)

Jesli taka zaleznosc zajdzie dla kazdego wierzcholka, czyli dana formula bedzie spelnialna dla kazdego wierzcholka
to znaczy, ze da sie utworzyc serie takich wyscigow

tworze graf ktorego wierzcholkami sa iteraly oraz ich zaprzeczenia (iteralami beda krawedzie), interpretujac
x=>~y jako krawedz (x,~y) i szukam poprwanego wartosciowania

Robie to szukajac silnie spojnych skladowych, jesli bedzie istniec silna spojna skladowa, w ktorej wystapi para
iteralow komplemetarnych, to formula jest niespelnialna, bo wybranie iteralu x wymusza wybranie iteralu ~x, to daje sprzecznosc

Jesli takiej spojnej skladowej nie bedzie, to beda istniec jedynie silnie spojne skladowe, w ktorych wybranie ktoregos iteralu
implikuje wybranie reszty z tej skladowej, ale w poprawny sposob, lub sciezki, w ktorych wybranie jednego wartosciowania implukuje
reszte iteralow w sciezce, oraz za kazdym razem da sie poprawnie wybrac poczatek tej sciezki, a to wszystko znaczy, ze bedzie
istniec poprawne wartosciowanie, wiec i poprawny podzial wyscigow

|Jesli itnieje (x,y), to istnieje (~y, ~x)|
Stanie sie tak, poniewaz jesli istnieje sciezka z x do a, oraz z a do ~x: ( x, x1, x2, ..., xm, a ), (a, y1, y2, ..., yn, ~x)
|zakladajac, ze xi ~= ~xj oraz yi != ~yj, ale jesli maja, to dla nich rekurencyjnie mozna rozwiazac ten problem|
Wiec zamiast isc od x do a, a potem od a do ~x, moge wybrac sciezki x1 do a, oraz a do ~x i otrzymam poprawne wartosciowanie
dla kazdego iteralu, wiec i poprawne rozwiazanie

Jesli do jakiegos wierzcholka wchodzi, lub wychodzi tylko jedna droga, to oznaczam, ze musi ona byc wzieta, i nie uwzgledniam jej
w formule, ale oznaczam ze biore tworzac z kazdego pozostalego wierzcholka krawedz do niej, aby wszystko implikowalo wziecie jej
a nie - nie wziecie jej
"""