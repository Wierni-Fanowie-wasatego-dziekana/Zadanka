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


def komunia(A,B):
    tabliczka = Node(None)
    A1 = A
    B1 = B
    while A is not None and B is not None:
        if not B1.obecnosciowanko(A.val):
            tabliczka.dodawanko(A.val)
        if not A1.obecnosciowanko(B.val):
            tabliczka.dodawanko(B.val)
        A = A.next
        B = B.next
    while A is not None:
        if not B1.obecnosciowanko(A.val):
            tabliczka.dodawanko(A.val)
        A = A.next

    while B is not None:
        if not A1.obecnosciowanko(B.val):
            tabliczka.dodawanko(B.val)
        B = B.next

    return tabliczka.next

lista = Node(22)  # wartownik
lista.dodawanko(16) # To jest pańska ocena
lista.dodawanko(13) # O tej ocenie możesz porozmawiać pod biurkiem
lista.dodawanko(2)


lista2 = Node(0)
lista2.dodawanko(2) # To jest pańska ocena
lista2.dodawanko(3)
lista2.dodawanko(13)
lista2.dodawanko(16)
#lista2.dodawanko(25)

listuuunia = komunia(lista,lista2)
listuuunia.printowanko()