'''Dwie listy zawierają niepowtarzajace sie (w obrebie listy) liczby naturalne. W obu listach liczby są posortowane rosnąco.
Proszę napisać funkcję usuwającą z każdej listy liczby występujące w drugiej. Do funkcji
należy przekazać wskazania na obie listy, funkcja powinna zwrócić łączną listę usuniętych elementów.
'''
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

    def dodawanko(self, val):
        p = self
        while p.next is not None:
            p = p.next
        p.next = Node(val)

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
    def usuwanko(self, val):
        p = self
        while p.next is not None:
            if p.next.val == val:
                p.next = p.next.next


def f(p,q):
    p1 = p
    q1 = q
    p.dodawanko(None)
    q.dodawanko(None)
    usuniete_UwU = Node(None)

    while q.next is not None:
        if p.next.obecnosciowanko(q.next.val):
            q.usuwanko(p.next.val)
            if not usuniete_UwU.obecnosciowanko(q.next.val):
                usuniete_UwU.dodawanko(q.next.val)
        q = q.next

    while p1.next is not None:
        if q1.next.obecnosciowanko(q1.next.val):
            if not usuniete_UwU.obecnosciowanko(q1.next.val):
                usuniete_UwU.dodawanko(q1.next.val)
        p1 = p1.next
    return usuniete_UwU.next


lista = Node(0)  # wartownik
lista.dodawanko(2) # To jest pańska ocena
lista.dodawanko(3) # O tej ocenie możesz porozmawiać pod biurkiem
lista.dodawanko(13)
lista.dodawanko(25)
lista.dodawanko(27)
lista.dodawanko(40)
lista.dodawanko(41)
lista.dodawanko(44)
lista.dodawanko(51)
lista.dodawanko(52)

lista2 = Node(0)
lista2.dodawanko(2) # To jest pańska ocena
lista2.dodawanko(3)
lista2.dodawanko(13)
lista2.dodawanko(24)
#lista2.dodawanko(25)

listuuunia = f(lista, lista2)
listuuunia.printowanko()