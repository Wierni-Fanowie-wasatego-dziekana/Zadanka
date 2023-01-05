class Node():
    def __init__(self,val,next = None):
        self.val = val
        self.next = next

    def dodawanko(self,val):
        p = self
        while p.next != None:
            p = p.next
        p.next = Node(val)

    def szukanko(self,value):
        p = self
        while p.next is not None:
            if p.val == value:
                return True
            p = p.next
        return False

    def usuwanko(self, value):
        p = self
        while p.next is not None and p.next.val != value:
            p = p.next
        if p.next.val == value:
            p.next = p.next.next

    def printowanko(self):
        p = self
        if p.val is None:
            p = p.next
        while p is not None:
            print(p.val)
            p = p.next

def zad11(lista, val):
    while lista.next is not None and lista.next.val != val:
        lista = lista.next
    if lista.next is not None:
        lista.usuwanko(val)
    else:
        lista.dodawanko(val)

    return lista

lista1 = Node(3)
lista1.dodawanko(4)
lista1.dodawanko(6)
lista1.dodawanko(7)
lista1.dodawanko(6)
lista1.printowanko()
print('----')

zad11(lista1, 4)
lista1.printowanko()

