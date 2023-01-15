

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


def ostrowiec(header):
    p = header
    tab = [Node() for _ in range(10)]
    while p is not None:
        tab[p.val%10].dodawanko(p.val)
        p=p.next
    res = Node(None)
    for i in range(10):
        tab[i]=tab[i].next
        while tab[i] is not None:
            res.dodawanko(tab[i].val)
            tab[i] = tab[i].next
    return res.next

lista = Node(22)  # wartownik
lista.dodawanko(10) # To jest pańska ocena
lista.dodawanko(13) # O tej ocenie możesz porozmawiać pod biurkiem
lista.dodawanko(2)
lista.dodawanko(1)
lista.dodawanko(3)
lista.dodawanko(6)
lista.dodawanko(9)
lista.dodawanko(8)
lista.dodawanko(7)
lista.dodawanko(5)

listuunia = ostrowiec(lista)
listuunia.printowanko()