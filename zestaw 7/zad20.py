'''Dana jest lista zawierająca ciąg obustronnie domkniętych przedziałów.
Krańce przedziałów określa uporządkowana para liczb całkowitych. Proszę
napisać stosowne deklaracje oraz funkcję redukującą liczbę elementów listy.
Na przykład lista: [15,19] [2,5] [7,11] [8,12] [5,6] [13,17]
powinien zostać zredukowany do listy: [13,19] [2,6] [7,12]
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



def redukcjunio(header):
    p = q = header
    wynikunio = Node(None)
    while p.next is not None:
        q = p.next
        while q is not None:
            res = zawierunio(p.val, q.val)
            if res is not False:
                if not(wynikunio.obecnosciowanko(res)):
                    wynikunio.dodawanko(res)
            q = q.next
        p = p.next

    return wynikunio


def zawierunio(a,b):
    flagunia = False
    if a[0] < b[0] < a[1] or a[0] < b[1] < a[1] or b[0] < a[0] < b[1] or b[0] < a[1] < b[1]:
        a[0] = min(a[0], b[0])
        a[1] = max(b[1], a[1])
        flagunia = True
    elif a[0] == b[1] or b[0] == a[1]:
        a[0] = min(a[0], b[0])
        a[1] = max(b[1], a[1])
        flagunia = True
    elif a[0] == b[0]:
        a[1] = max(a[1], b[1])
        flagunia = True
    elif a[0] == b[0] and a[1] == b[1]:
        flagunia = True
    elif a[1] == b[1]:
        a[0] = min(a[0], b[0])
        flagunia = True

    if flagunia:
        return a
    else:
        return False


listunia = Node([15,19])
listunia.dodawanko([7,11])
listunia.dodawanko([2,5])
listunia.dodawanko([5,6])
listunia.dodawanko([8,12])
listunia.dodawanko([13,17])

listunia = redukcjunio(listunia)
listunia.next.printowanko()
