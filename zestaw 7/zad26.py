'''Proszę napisać funkcję, która sprawdza czy jedna lista zawiera się w
drugiej. Do funkcji należy przekazać wskazania na pierwsze elementy obu
list, funkcja powinna zwrócić wartość logiczną.'''


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

def wasacz(p,q):
    p1 = p
    q1 = q
    # # ktora jest dluzsza
    # while p is not None:
    #     p = p.next
    #     cunt_p += 1
    # while q is not None:
    #     q = q.next
    #     cunt_q += 1

    while p is not None and q is not None:
        p, q = p.next, q.next
    if p is None and q is None: # sa rowne
        longer = q1
        shorter = p1
    elif p is None:   # p jest krótsze
        longer = q1
        shorter = p1
    else:   # q jest krótsze
        longer = p1
        shorter = q1

    while longer is not None:
        if longer.val == shorter.val:
            shorter_prime = shorter
            longer_prime = longer
            while shorter_prime is not None and longer_prime.val == shorter_prime.val:
                shorter_prime = shorter_prime.next
                longer_prime = longer_prime.next
            if shorter_prime is None:
                return True
        longer = longer.next

    return False


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
lista2 = Node(211)  # To jest pańska ocena

lista2.dodawanko(211)
lista2.dodawanko(997)
lista2.dodawanko(199)
lista2.dodawanko(199)

lista2.printowanko()
print()
print(wasacz(lista2,lista))

