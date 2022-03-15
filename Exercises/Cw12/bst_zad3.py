"""
Tworze przenumerowanie
G - 0
T - 1
A - 2
C - 3

Kazde bialko traktuje na liczbe o podstawie 4
np GATTCCA
0*4^6 + 2*4^5 + 1*4^4 + 1*4^3 + 3*4^2 + 3*4^1 + 2*4^0

Kazde z bialemk bedzie posiadac swoja jednoznaczna reprezentacje
Teraz uzywajac tych reprezentacji jako kluczy umieszczam konkretne bialka w drzewie bst
dopoki przy wstawianiu nie zoorientuje sie, ze jakies bialko juz istnieje, wtedy zwracam falsz
Jesli wloze wszystkie bialka i nie znajde duplikatu zwracam prawde
"""

"""
Drugi pomysl to tworzenie drzewa bst, w ktorym kazdy node posiadac bedzie 4 dzieci odpowiadajacych literkom GTAC
Gdy wsadzam jakies nowe bialko do drzewa, wedruje po drzewie po literkach ktore juz w nim sa az dotre do momentu bialka,
ktoro w drzewie jeszcze nie zostalo dopisane, to dodaje mu odpowiednie dzieci tworzac ciag dalszy bialka

W kazdym Nodzie oprocz kluczy bedacych literkami, w wartosci przechowuje ilosc bialek zaczynajacych sie od korzenia
i konczacych sie w tym Nodzie, dzieki temu gdy wkladam nowe bialko do drzewa, i wszystkie jego literki juz sa wpisane
jestem w stanie okreslic, czy jakies bialko juz wczesniej skonczylo sie w tym samym miejscu, czyli czy istnieje duplikat
"""