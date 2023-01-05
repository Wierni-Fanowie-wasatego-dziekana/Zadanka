'''Dana jest niepusta lista reprezentująca liczbę naturalną. Kolejne
elementy listy przechowują kolejne cyfry. Proszę napisać funkcję
zwiększającą taką liczbę o 1.
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

def zwiekszanko(L, ind=0):
    if L.next is None:
        L.val = (L.val + 1)%10
        return
    zwiekszanko(L.next,ind+1)
    if L.next.val == 0:
        L.val = (L.val + 1) % 10
    if ind == 0 and L.val == 0:
        L1 = Node(1)
        while L is not None:
            L1.dodawanko(L.val)
            L = L.next
        return L1
    return L

lista = Node(2)  # To jest pańska ocena
lista.dodawanko(997)
lista.dodawanko(213)
lista.dodawanko(2115)
lista.dodawanko(420)
lista.dodawanko(69)
lista.printowanko()