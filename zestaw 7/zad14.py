'''Proszę napisać funkcję, otrzymującą jako parametr wskaźnik na pierwszy
element listy o wartościach typu int, usuwającą wszystkie elementy, których
wartość dzieli bez reszty wartość bezpośrednio następujących po nich
elementów. '''
class Node:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next

    def dodawanko(self, val):
        p = self
        while p.next is not None:
            p = p.next
        p.next = Node(val)

    def usuwanko(self, val):
        p = self
        while p.next.val != val and p.next is not None:
            p = p.next
        if p.next.val == val:
            p.next = p.next.next


    def obecnosciowanko(self,val):
        q = self
        while q is not None:
            if q.val == val:
                return True
            q = q.next
        return False

    def printowanko(self):
        q = self
        while q is not None:
            print(q.val)
            q = q.next


def f(header):
    p = header
    q = p
    val_holder = None
    while p is not None and p.next is not None:
        if p.next.val % p.val == 0:
            val_holder = p.next.val
            p.next = p.next.next
            while p.next is not None and p.next.val % val_holder == 0:
                val_holder = p.next.val
                p.next = p.next.next

        p = p.next

    return q


lista = Node(2)  # To jest pańska ocena
lista.dodawanko(3)
lista.dodawanko(6)
lista.dodawanko(9)
lista.dodawanko(2115)
lista.dodawanko(33)
lista.dodawanko(66)
lista.printowanko()
lista = f(lista)
print('------')

lista.printowanko()
