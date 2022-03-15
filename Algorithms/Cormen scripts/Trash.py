from random import randint
class Node:
    def __init__(self):
        self.value = None
        self.next = None

def print_list(pointer):
    while pointer is not None:
        print(pointer.value, end=' -> ')
        pointer = pointer.next
    print('|')

def tab2list(tab):
    head = Node()
    pointer = head
    for i in range(len(tab)):
        new = Node()
        new.value = tab[i]
        pointer.next = new
        pointer = pointer.next
    pointer.next = None
    return head.next

#tu tz mamy wartownika
def app(pointer, value):
    new_node = Node()
    new_node.value = value

    while pointer.next is not None:
        pointer = pointer.next
    pointer.next = new_node


def find_min_max(pointer):
    counter = 0
    min_val = pointer.value
    max_val = pointer.value
    while pointer is not None:
        if   pointer.value < min_val: min_val = pointer.value
        elif max_val < pointer.value: max_val = pointer.value
        pointer = pointer.next
        counter += 1
    return min_val, max_val, counter