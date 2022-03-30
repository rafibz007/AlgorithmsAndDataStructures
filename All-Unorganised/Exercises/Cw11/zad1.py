"""
(x v y) == (~x=>y) ^ (~y=>x)
tworze wierzcholki dla kazdego iteralu, oraz jego zaprzeczenia
analizujac wejsciowa formule przeksztalacam ja na implikacje, ktore w moim grafie beda odpowiadac za dane wierzcholki skierowane
np ~x=>y odpowiada za krawedz (~x, y)

Jesli w takim grafie istnieje silnia spojna skladowa, zawierajaca w sobie iteraly komplementarne, to formula
jest niespelnialna, w przeciwnym razie, jest spelnialna

Bedzie tak, dlatego, ze jesli istnieje taka silna spojna skladowa, to nie wazne dla jakiego wartosciowania, pewna zmienna
bedzie musiala zostac wybrana jako ona i jej zaprzeczenie, co daje sprzecznosc

Jesli takiej slinie spojnej skladowej nie bedzie, to zmienne beda nalezec do spojnej skladowej dla ktorej wybor jednego iteralu
wymusi wybor reszty w tej spojnej, ale bedzie on poprawny, albo beda nalezec do sciezki, w ktorej wybor jednego iteralu implikuje
wybor reszty, nawet jesli w sciezke wystepuje para iteralow, komplementarnych to wziecie sciezki od pewnego momentu
tak aby zawierala wartosciowanie kazdego iteralu dokladnie raz da poprawny wynik

|Jesli itnieje (x,y), to istnieje (~y, ~x)|
Stanie sie tak, poniewaz jesli istnieje sciezka z x do a, oraz z a do ~x: ( x, x1, x2, ..., xm, a ), (a, y1, y2, ..., yn, ~x)
|zakladajac, ze xi ~= ~xj oraz yi != ~yj, ale jesli maja, to dla nich rekurencyjnie mozna rozwiazac ten problem|
Wiec zamiast isc od x do a, a potem od a do ~x, moge wybrac sciezki x1 do a, oraz a do ~x i otrzymam poprawne wartosciowanie
dla kazdego iteralu, wiec i poprawne rozwiazanie


Wiec w obu tych przypadkach formula jest spelnialna
"""