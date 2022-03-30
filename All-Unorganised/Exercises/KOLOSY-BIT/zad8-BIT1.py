class Node:
    def __init__(self):
        self.value = None
        self.next = None


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

#tu tz mamy wartownika
def app(pointer, value):
    new_node = Node()
    new_node.value = value

    while pointer.next is not None:
        pointer = pointer.next
    pointer.next = new_node

#bedzie miala wartownika
def selection_sort(head):
    new_head = Node()
    new_pointer = new_head
    while head.next is not None:
        pointer = head.next
        prev = head
        min_pointer = pointer
        min_prev = prev
        while pointer is not None:
            if min_pointer.value > pointer.value:
                min_pointer = pointer
                min_prev = prev
            prev = pointer
            pointer = pointer.next
        new_pointer.next = min_pointer
        new_pointer = new_pointer.next
        min_prev.next = min_pointer.next
    return new_head


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


def sort(pointer):

    min_val, max_val, length = find_min_max(pointer)
    value_range = (max_val - min_val)/length
    buckets = [ Node() for _ in range(length) ]
    while pointer is not None:
        ratio = ((pointer.value-min_val)/value_range)
        diff = ratio - int(ratio)
        # print(int(ratio))
        if diff == 0 and pointer.value != min_val:
            app(buckets[ int(ratio)-1 ], pointer.value)
        else: app(buckets[ int(ratio) ], pointer.value)
        pointer = pointer.next

    # print("--------")
    new_head = Node()
    new_pointer = new_head
    for bucket in buckets:
        # print_list(bucket)
        bucket = selection_sort(bucket)
        # print_list(bucket)
        new_pointer.next = bucket.next
        while new_pointer.next is not None: new_pointer = new_pointer.next
    return new_head.next

#
# L = tab2list([1,2 ,3 ,4, 5, -1, 5, 8, 2])
# print_list(L)
# L = selection_sort(L)
# print_list(L)

L = tab2list([1,2 ,3 ,4, 5, -1, 5, 8, 2,5, 687,34, 25, 67,-23 ,-4646, 0.14, 0])
print_list(L)
L = sort(L)
print_list(L)


# b = []
# # new = Node()
# b.append( Node() )
# app(b[0], 3)
# # print_list(b[0])

