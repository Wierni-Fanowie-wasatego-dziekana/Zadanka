''' Proszę napisać funkcję, która rozdziela elementy listy odsyłaczowej do
10 list, według ostatniej cyfry pola val. W drugim kroku powstałe listy
należy połączyć w jedną listę odsyłaczową, która jest posortowana
niemalejąco według ostatniej cyfry pola val.
'''''

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



def podzielenie(L):
    tab = [Node() for _ in range(10)]
    while L is not None:
        tab[L.val % 10].dodawanko(L.val)
        L = L.next
    # for i in range(10):
    #     # tab[i].printowanko()
    #     # print("end")
    L1 = Node()
    for i in range(10):
        while tab[i] is not None:
            if tab[i].val is not None:
                L1.dodawanko(tab[i].val)
            tab[i] = tab[i].next
    L1 = L1.next
    return L1


lista = Node(2)  # To jest pańska ocena
lista.dodawanko(997)
lista.dodawanko(2137)
lista.dodawanko(2115)
lista.dodawanko(420)
lista.dodawanko(69)
lista.printowanko()

lista1 = podzielenie(lista)

print()
lista1.printowanko()