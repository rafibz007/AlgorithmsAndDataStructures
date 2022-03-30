from random import randint, seed


class Node:
    def __init__(self):
        self.next = None
        self.value = None


def qsort(L):
    head = Node()
    head.next = L

    def recursive_quick_sort(begin_prev, end_next):  #funkcja dostaje wskaznik na element przed rozpoczeciem podzialu i zaraz po
                                                     #aby spartycjonowany fragment mozna bylo spowroem wpiac do tablicy
        while begin_prev.next != end_next:
            left, right = partition(begin_prev, end_next)

            recursive_quick_sort(begin_prev, left)

            #pozbywam sie rekursji ogonowej
            begin_prev = right
            left = end_next

            # recursive_quick_sort(right, end_next) - z rekursja ogonowa
    #endDEF

    def partition(begin_prev, end_next):

        pointer = begin_prev.next  # wskaznik pointer wskazuje na Noda od ktorego chcemy dzielic/sortowac/partycjonowac

        # 3 nowe listy na 3 "sekcje" dzielonej tablicy
        high_head = high = Node()  # wartosci wieksze od pivota
        low_head = low = Node()  # wartosci mniejsze od pivota
        equal_head = equal = Node()  # wartosci rowne pivotowi

        # rodzielanie tablicy od wskaznika pointer do end do 3 list w zaleznosci od wartosci ich noda
        pivot = pointer.value
        while pointer != end_next:
            if pointer.value < pivot:
                low.next = pointer
                low = low.next
            elif pointer.value > pivot:
                high.next = pointer
                high = high.next
            else:
                equal.next = pointer
                equal = equal.next
            pointer = pointer.next

        # laczenie powstalych 3 list w jedna nowa zachowujac porzadek low,equal,high
        low.next = equal_head.next
        equal.next = high_head.next

        # przyczepienie nowej listy z powrotem do starej
        if equal.next is None: equal.next = end_next
        else: high.next = end_next
        begin_prev.next = low_head.next

        return equal_head.next, equal  # zwraca wskazniki na: 1)pierwszy element sekcji piwotow, 2)ostatni element sekcji piwotow
    #endDEF

    recursive_quick_sort(head, None)
    return head.next
#endDEF


def tab2list(A):
    H = Node()
    C = H
    for i in range(len(A)):
        X = Node()
        X.value = A[i]
        C.next = X
        C = X
    return H.next


def printlist(L):
    while L != None:
        print(L.value, "->", end=" ")
        L = L.next
    print("|")


seed(42)

n = 1000
T = [randint(1, 10) for i in range(n)]
L = tab2list(T)

print("przed sortowaniem: L =", end=" ")
# printlist(L)
L = qsort(L)
print("po sortowaniu    : L =", end=" ")
# printlist(L)

if L == None:
    print("List jest pusta, a nie powinna!")
    exit(0)

P = L
while P.next != None:
    if P.value > P.next.value:
        print("Błąd sortowania")
        exit(0)
    P = P.next

print("OK")

