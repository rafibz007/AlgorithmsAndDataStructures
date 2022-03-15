class Node:
    def __init__(self, value):
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


#zakladam ze ma wartownika
def get_max(head):
    prev_max = head
    pointer_max = head.next

    prev = head
    pointer = head.next

    while pointer is not None:
        if pointer.value > pointer_max.value:
            prev_max = prev
            pointer_max = pointer
        prev = pointer
        pointer = pointer.next

    prev_max.next = pointer_max.next
    return pointer_max


def sort(pointer):
    #chwilowi wartownicy
    unsorted_head = Node("W")
    unsorted_head.next = pointer

    sorted_head = Node("W")

    while unsorted_head.next is not None:
        node_max = get_max(unsorted_head)
        node_max.next = sorted_head.next
        sorted_head.next = node_max

    return sorted_head.next

my_list = create([10,45,67,2,4,15,7,35,7,4,26,7,23])
print_list(my_list)
my_list = sort(my_list)
print_list(my_list)





