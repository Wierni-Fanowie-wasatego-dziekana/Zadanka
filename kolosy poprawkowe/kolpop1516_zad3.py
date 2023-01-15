''' Dany jest zbiór punktów płaszczyzny o współrzędnych będących liczbamicałkowitymi.7bior
ten dany jest w postaci listy jednokierunkowej. Proszę funkcję, która rozdziela łańcuch na cztery
łańcuchy zawierające punkty należące odpowiednio do l,ll,lll i lV ćwiartki układu współrzędnych,
natomiast punkty leżące na osiach układu współrzędnych usuwa z pamięci. Proszę zadeklarować
odpowiednie typy.'''


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


def ds16itaka(header, cw1, cw2, cw3, cw4):
    while header is not None and header.next is not None:
        a = header.next.val
        if a[0] > 0:
            if a[1] > 0:
                cw1.dodawanko(a)
            elif a[1] < 0:
                cw4.dodawanko(a)
        elif a[0] < 0:
            if a[1] > 0:
                cw2.dodawanko(a)
            elif a[1] < 0:
                cw3.dodawanko(a)
        if a[0] == 0 or a[1] == 0:
            if header.next is not None and header.next.next is not None:
                header.next = header.next.next
            else:
                header.next = None
        header = header.next


lista = Node(None)
lista = Node((15, 16))  # wartownik
lista.dodawanko((10, 160)) # To jest pańska ocena
lista.dodawanko((-5, 15)) # O tej ocenie możesz porozmawiać pod biurkiem
lista.dodawanko((-2,-1))
lista.dodawanko((12,-1))
lista.dodawanko((-2,0))
lista.dodawanko((-2,1))
lista.dodawanko((0,-1))
lista.dodawanko((-3,-18))
lista.dodawanko((12,12))
lista.dodawanko((12,-1))
lista.dodawanko((-2,12))
lista.dodawanko((0,0))

cw1 = Node()
cw2 = Node()
cw3 = Node()
cw4 = Node()
ds16itaka(lista, cw1, cw2, cw3, cw4)
lista.printowanko()
print()
cw1.next.printowanko()
print()
cw2.next.printowanko()
print()
cw3.next.printowanko()
print()
cw4.next.printowanko()