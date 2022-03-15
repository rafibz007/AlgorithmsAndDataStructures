'''Proszę zaimplementować  scalanie dwóch posortowanych list jednokierunkowych do jednej'''

class Node:
  def __init__(self,value=None):
    self.value = value
    self.next = None

  def __str__(self):
    strr = "["
    p = self
    while p is not None:
      strr = strr + str(p.value) + " "
      p = p.next
    strr += "]"
    return strr

def create(tab):
    wart = Node("W")
    pointer = wart
    for el in tab:
        pointer.next = Node(el)
        pointer = pointer.next
    return wart.next

def merge(p1, p2):
    W = Node("W")
    pointer = W
    while p1 is not None and p2 is not None:
        if p1.value < p2.value:
            pointer.next = p1
            p1 = p1.next
        else:
            pointer.next = p2
            p2 = p2.next
        pointer = pointer.next

    if p1 is not None:
        pointer.next = p1
    else:
        pointer.next = p2

    return W.next


def cut(pointer): #return cut_off rest_of_list
    head = pointer
    prev = None
    while pointer.next is not None:
        prev = pointer
        pointer = pointer.next
        if prev.value > pointer.value:
            prev.next = None
            return head, pointer
    return head, None


t1 = create([-10, -5, 0, 5, 7, 9, 78])
t2 = create([4,5 ,6,67 ,86 ,889, 45, 45,23 , 35, -34])
print(t1)
print(t2)
print(merge(t1, t2))
x, y = cut(t2)
print(x,y)