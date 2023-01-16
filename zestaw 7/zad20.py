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
    p = header
    q = header
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


def zawierunio(p,q):
    return (min(p[0], q[0]), max(p[1], q[1])) if p[1] >= q[0] and q[1] >= p[0] else None

def overlap(p1, p2):
    return (p1[0] <= p2[0] <= p1[1] or p1[0] <= p2[1] <= p1[1]
            or p2[0] <= p1[0] <= p2[1] or p2[0] <= p1[1] <= p2[1])

# def funkcja(header):
#     p = header
#     bq = p
#     q = bq.next
#     flag = False
#     while True:
#         while q is not None:
#             if overlap(p.val, q.val):
#                 p.val[0] = min(p.val[0], q.val[0])
#                 p.val[1] = max(p.val[1], q.val[1])
#                 bq.next = q.next
#                 q = q.next
#                 flag = True
#             else:
#                 bq = q
#                 q = q.next
#         if not flag and p.next is None:
#             return header
#         elif p.next is not None:
#             p = p.next
#             bq = p
#             q = bq.next
#         else:
#             return header
#

listunia = Node([15,19])
listunia.dodawanko([20,21])
listunia.dodawanko([18,20])
listunia.dodawanko([5,6])
listunia.dodawanko([8,12])
listunia.dodawanko([13,14])
listusiaaaaa = redukcjunio(listunia)
#funkcja(listunia)
listusiaaaaa.next.printowanko()
