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


def quick_sort( head ):

    def sort( beg_prev, end_next ):
        if beg_prev.next is not end_next:
            pivot_beg, pivot_end = partition(beg_prev, end_next)
            sort(beg_prev, pivot_beg)
            sort(pivot_end, end_next)

    def partition( beg_prev, end_next ):
        new_lower = Node()
        new_equal = Node()
        new_greater = Node()

        pointer_lower = new_lower
        pointer_equal = new_equal
        pointer_greater = new_greater

        pointer = beg_prev.next
        pivot = pointer.value

        while pointer is not end_next:
            if pointer.value < pivot:
                pointer_lower.next = pointer
                pointer_lower = pointer_lower.next
            elif pointer.value > pivot:
                pointer_greater.next = pointer
                pointer_greater = pointer_greater.next
            else:
                pointer_equal.next = pointer
                pointer_equal = pointer_equal.next
            pointer = pointer.next


        pointer_lower.next = new_equal.next
        pointer_equal.next = new_greater.next

        if pointer_equal.next is None:
            pointer_equal.next = end_next
        else: pointer_greater.next = end_next
        beg_prev.next = new_lower.next


        return new_equal.next, pointer_equal


    sort(head, None)
    return head

T = [ 9, 10, 4, 56, 23, 5, 1, 0, -1, 23, -45, -2, 12, -5, 7, 1 ]
P = create_list(T)
print_list(P)
P = quick_sort(P)
print_list(P)