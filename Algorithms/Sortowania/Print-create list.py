#zakladam ze jest wartownik

class Node:
    def __init__(self, value="W"):
        self.next = None
        self.value = value


def print_list(pointer):
    while pointer is not None:
        print(pointer.value, end=' ')
        pointer = pointer.next
    print('')


def create_list( T ):
    new_head = Node()
    pointer = new_head
    for i in range(len(T)):
        pointer.next = Node( T[i] )
        pointer = pointer.next
    return new_head