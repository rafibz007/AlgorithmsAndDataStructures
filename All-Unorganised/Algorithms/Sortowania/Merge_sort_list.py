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


def merge_sort( head ):

    def cut_increasing_seq( pointer ):
        start_of_seq = pointer
        while pointer.next is not None:
            if pointer.next.value < pointer.value:
                break
            pointer = pointer.next

        rest = pointer.next
        pointer.next = None
        return start_of_seq, rest

    def merge( p1, p2 ):
        new_head = Node()
        pointer = new_head
        while p1 is not None and p2 is not None:
            if p2.value < p1.value:
                pointer.next = p2
                p2 = p2.next
            else:
                pointer.next = p1
                p1 = p1.next
            pointer = pointer.next

        if p1 is not None:
            pointer.next = p1

        if p2 is not None:
            pointer.next = p2

        return new_head.next


    while True:
        new_head = Node()
        new_pointer = new_head
        pointer = head.next

        number_of_cuts = 0

        while pointer is not None:
            seq1, pointer = cut_increasing_seq(pointer)
            number_of_cuts += 1

            if pointer is None:
                new_pointer.next = seq1
                break

            seq2, pointer = cut_increasing_seq(pointer)
            number_of_cuts += 1

            result = merge(seq1, seq2)

            new_pointer.next = result
            while new_pointer.next is not None:
                new_pointer = new_pointer.next



        if number_of_cuts == 1:
            head.next = new_head.next
            return head

        head = new_head

T = [ 9, 10, 4, 56, 23, 5, 1, 0, -1, 23, -45, -2, 12, -5, 7 ]
P = create_list(T)
print_list(P)
P = merge_sort(P)
# merge_sort(P)
print_list(P)