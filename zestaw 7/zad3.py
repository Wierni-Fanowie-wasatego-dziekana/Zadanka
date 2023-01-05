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


def scalankoit(L1, L2):
    q = L1
    p = L2
    scalona = Node()
    while q is not None and p is not None:
        if q.val < p.val:
            scalona.dodawanko(q.val)
            q = q.next
        elif p.val < q.val:
            scalona.dodawanko(p.val)
            p = p.next
        else:
            scalona.dodawanko(p.val)
            scalona.dodawanko(q.val)
            q = q.next
            p = p.next
    while p is not None:
        scalona.dodawanko(p.val)
        p = p.next
    while q is not None:
        scalona.dodawanko(q.val)
        q = q.next
    return scalona


def scalankorek(L1, L2, scalona=Node()):
    if L1 is None and L2 is None:
        return scalona
    if L1 is not None and L2 is not None:
        if L1.val < L2.val:
            scalona.dodawanko(L1.val)
            return scalankorek(L1.next,L2,scalona)
        elif L2.val < L1.val:
            scalona.dodawanko(L2.val)
            return  scalankorek(L1, L2.next, scalona)
        else:
            scalona.dodawanko(L2.val)
            scalona.dodawanko(L1.val)
            return scalankorek(L1.next,L2.next,scalona)

    if L1 is not None:
        scalona.dodawanko(L1.val)
        return scalankorek(L1.next,L2,scalona)
    if L2 is not None:
        scalona.dodawanko(L2.val)
        return scalankorek(L1,L2.next, scalona)


lista1 = Node(1)
lista1.dodawanko(3)
lista1.dodawanko(4)
lista1.dodawanko(5)
lista1.dodawanko(100)
lista1.dodawanko(101)
lista1.dodawanko(102)

lista2 = Node(2)
lista2.dodawanko(3)
lista2.dodawanko(6)
lista2.dodawanko(7)

listait = scalankoit(lista1, lista2)
listait.printowanko()
print()
listarek=scalankorek(lista1,lista2)
listarek.printowanko()

