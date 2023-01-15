'''Proszę napisać funkcję scalającą dwie posortowane listy w jedną
posortowaną listę. Do funkcji należy przekazać wskazania na pierwsze
elementy obu list, funkcja powinna zwrócić wskazanie do scalonej listy.
- funkcja iteracyjna,
- funkcja rekurencyjna.'''

class Node:
    def __init__(self, val=None, next=None):
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

    def obecnosciowanko(self, val):
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


def pizdnie(p,q):
    nowa_lista = Node()
    while p is not None and q is not None:
        if p.val < q.val:
            nowa_lista.dodawanko(p.val)
            p = p.next
        else:
            nowa_lista.dodawanko(q.val)
            q = q.next

    if p is None:
        while q is not None:
            nowa_lista.dodawanko(q.val)
            q = q.next
    else:
        while p is not None:
            nowa_lista.dodawanko(p.val)
            p = p.next
    return nowa_lista.next

lista = Node(2)  # To jest pańska ocena
lista.dodawanko(13)
lista.dodawanko(25)
lista.dodawanko(27)
lista.dodawanko(40)
lista.dodawanko(41)
lista.dodawanko(44)
lista.dodawanko(51)
lista.dodawanko(51)
lista.dodawanko(51)
lista.dodawanko(52)

lista2 = Node(3)  # To jest pańska ocena
lista2.dodawanko(5)
lista2.dodawanko(7)
lista2.dodawanko(13)
lista2.dodawanko(24)

listuuunia = pizdnie(lista, lista2)
listuuunia.printowanko()

