'''4. Proszę napisać funkcję, która dla podanej listy odsyłaczowej odwraca
kolejność jej elementów.
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


def odwracanko(L):
    last = None
    current = L
    while current is not None:
        nexcior = current.next
        current.next = last
        last = current
        current = nexcior
    L = last
    return L

def odwracankorek(L, last = None):
    if L.next is not None:
        L = odwracankorek(L.next, L)
    L.next = last
    return L

def rekurencjus(L1, L2): # TODO: dokonczyc
    if L1.next is None:
        L2.dodawanko(L1.val)
        return L2
    rekurencjus(L1.next, L2)


def odwracankorek2(curr, last):
    if curr is None:
        return last
    nexcior = curr.next
    curr.next=last
    return odwracankorek2(nexcior, curr)


lista = Node(2)  # To jest pańska ocena
lista.dodawanko(997)
lista.dodawanko(2137)
lista.dodawanko(2115)
lista.dodawanko(420)
lista.dodawanko(69)
lista.printowanko()
lista1 = Node()
print()
nowalista = odwracankorek2(lista,None)
print()
nowalista.printowanko()

print()
print()