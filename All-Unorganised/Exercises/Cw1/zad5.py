class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

def create(T):
    head = Node("W") #chwilowy wartownik
    pointer = head
    for element in T:
        pointer.next = Node(element)
        pointer = pointer.next
    #endFOR
    return head.next


def print_list(pointer):
    while pointer.next is not None:
        print(pointer.value, "->", end=' ')
        pointer = pointer.next
    print(pointer.value)


def reverse(pointer):
    prev = None
    #after that while loop pointer will be None, and prev will be our new head of reversed list
    while pointer is not None:
        next_save = pointer.next
        pointer.next = prev
        prev = pointer
        pointer = next_save
    #endWHILE
    return prev

my_list = create([10,45,67,2,4,15,7,35,7,4,26,7,23])
print_list(my_list)
my_list = reverse(my_list)
print_list(my_list)