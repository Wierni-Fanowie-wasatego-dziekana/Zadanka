class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

    def dodawanko(self, val):
        p = self
        while p.next != None:
            p = p.next
        p.next = Node(val)

    def printowanko(self):
        p = self
        if p.val is None:
            p = p.next
        while p is not None:
            print(p.val)
            p = p.next


def trojkowy(n):
    T = [0] * 3
    while n != 0:
        T[n % 3] += 1
        n //= 3
    return T[1] > T[2]


def f(p):
    while p.next is not None:
        if trojkowy(p.next.val):
            p.next = p.next.next
        else:
            p = p.next
    return p

lista = Node(2)
lista.dodawanko(1)
lista.dodawanko(1)
lista.dodawanko(2)
lista.dodawanko(3)
lista.dodawanko(3)
lista.dodawanko(1)
lista.printowanko()
print('--------')
f(lista)
lista.printowanko()

' ------------------------------------------- '

class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next


def my_find(p,q,key):
    q.val = key

    res = rek(p, key)
    if res == q:
        return
    else:
        return res

def rek(p,key):
    if p.val == key:
        return p
    return rek(p.next,key)

def my_del(p,q,key):
    r = p
    if p.val == key:
         return p.next
    while p != p.next:
        if p.next.val == key:
            p.next = p.next.next
            return r
    return r