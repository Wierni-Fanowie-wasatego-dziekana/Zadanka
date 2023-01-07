class Node:
    def __init__(self,val,next=None):
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

def usuwanie_el(header):
    p = header
    w = p.dodawanko(None)
    cnt = 0
    while p.next is not None:
        if p.next.val == p.val:
            p = p.next
            cnt += 1
            while p is not None and p.next.val == p.val:
                if p.next.next.val is None:
                    cnt += 1
                    break
                p.next = p.next.next
                cnt += 1
        p = p.next
    return cnt

lista = Node(2)
lista.dodawanko(2) #
lista.dodawanko(3)
lista.dodawanko(4)
lista.dodawanko(5)
lista.dodawanko(5) #
lista.dodawanko(5) #
lista.dodawanko(5) #
lista.dodawanko(6)
lista.dodawanko(7)
lista.dodawanko(8)
lista.dodawanko(11)
lista.dodawanko(11) #
lista.dodawanko(69)
lista.dodawanko(69) #
lista.dodawanko(69) #
lista.dodawanko(69) #
lista.printowanko()

lista = usuwanie_el(lista)
print('----------')
print(lista)
