''' Proszę napisać funkcję, która pozostawia w liście wyłącznie elementy
unikalne. Do funkcji należy przekazać wskazanie na pierwszy element listy.
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


def chuj(header):
    wart = Node()
    while header is not None:
        if not(wart.obecnosciowanko(header.val)):
            wart.dodawanko(header.val)
        header = header.next

    return wart.next

def cipa(header):
    header.dodawanko(None) # zabezpieczenie przed usunieciem ostatniego
    p = header
    bq = p
    q = bq.next
    while p.next is not None:
        while q is not None:
            if p.val == q.val:
                bq.next = q.next
                q = q.next
            else:
                bq = q
                q = q.next
        p = p.next
        bq = p
        q = bq.next

    p = header
    while p.next.next is not None:
        p = p.next
    p.next = None

lista = Node(2)  # To jest pańska ocena
lista.dodawanko(997)
lista.dodawanko(211)
lista.dodawanko(211)
lista.dodawanko(211)
lista.dodawanko(997)
lista.dodawanko(199)
lista.dodawanko(199)
lista.dodawanko(2115)
lista.dodawanko(420)
lista.dodawanko(69)
lista.printowanko()

print()
cipa(lista)
lista.printowanko()