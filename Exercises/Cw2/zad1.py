from random import randint, seed

class Node:
    def __init__(self):
        self.value = None
        self.next = None


def merge_sorted_lists(p1, p2):
    head = Node()
    new_pointer = head

    while p1 is not None and p2 is not None:
        if p1.value <= p2.value:
            new_pointer.next = p1
            p1 = p1.next
        else:
            new_pointer.next = p2
            p2 = p2.next
        new_pointer = new_pointer.next

    if p1 is not None: new_pointer.next = p1
    else: new_pointer.next = p2

    while new_pointer.next is not None: new_pointer = new_pointer.next

    return head.next, new_pointer #zwraca pierwszy_node, ostatni_node


def cut(pointer):
    head = pointer
    prev = pointer
    while pointer is not None:
        if prev.value > pointer.value:
            prev.next = None
            break #to samo co: return head, pointer
        prev = pointer
        pointer = pointer.next

    return head, pointer #zwraca wskaznik na wyciaty element, wskaznik na reszte listy


def sorting(pointer):
    new_head = Node()
    new_last = new_head
    counter = 0

    while True:
        t1, pointer = cut(pointer)
        t2, pointer = cut(pointer)

        merged_poiner, merged_last = merge_sorted_lists(t1, t2)
        new_last.next = merged_poiner
        new_last = merged_last

        if pointer is None:
            pointer = new_head.next
            new_head = Node()
            new_last = new_head
            if counter == 1: break
            counter = 0
            # printlist(pointer)
        #endIF
        counter += 1
    #endWHILE

    return pointer


################

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


# seed(42)

n = 10
T1 = [randint(1, 10) for i in range(n)]
L1 = tab2list(T1)
printlist(L1)
L1 = sorting(L1)
printlist(L1)

