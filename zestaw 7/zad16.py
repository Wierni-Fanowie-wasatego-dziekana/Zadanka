class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

    def dodawanko(self, val):
        p = self
        while p.next is not None:
            p = p.next
        p.next = Node(val)

    def printowanko(self):
        q = self
        while q is not None:
            print(q.val)
            q = q.next
def osemeczka(n):
    T = [0] * 8
    while n != 0:
        T[n%8] += 1
        n //=8
    return T[5] % 2 == 0

def f(p):
    w1 = Node()
    w2 = Node()

    while p is not None:
        if osemeczka(p.val):
            w1.dodawanko(p.val)
        else:
            w2.dodawanko(p.val)
        p = p.next

    w1 = w1.next
    while w2 is not None:
        if w2.val is None:
            w2 = w2.next
        w1.dodawanko(w2.val)
        w2 = w2.next

    return w1


lista = Node(2)  # To jest pańska ocena
lista.dodawanko(997)
lista.dodawanko(213)
lista.dodawanko(2115)
lista.dodawanko(420)
lista.printowanko()

lista = f(lista)
print("----")
lista.printowanko()