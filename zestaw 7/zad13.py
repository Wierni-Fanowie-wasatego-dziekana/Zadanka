'''Proszę napisać funkcję, otrzymującą jako parametr wskaźnik na pierwszy
element listy o wartościach typu int, usuwającą wszystkie elementy, których
wartość jest mniejsza od wartości bezpośrednio poprzedzających je
elementów. '''

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


def funkcyjka(header):
     p = header
     q = p
     val_holder = None
     while p is not None and p.next is not None:
         if p.next.val < p.val:
            val_holder = p.next.val
            p.next = p.next.next
            while p.next is not None and val_holder > p.next.val:
                val_holder = p.next.val
                p.next = p.next.next

         p = p.next

     return q


lista = Node(2)  #
lista.dodawanko(98) #
lista.dodawanko(25)
lista.dodawanko(22)
lista.dodawanko(2115) #
lista.dodawanko(420)
lista.dodawanko(69)
lista.dodawanko(68)
lista.dodawanko(78) #
lista.dodawanko(307) #
lista.dodawanko(200)
lista.dodawanko(308) #
lista.dodawanko(280)
lista.dodawanko(322) #
lista.dodawanko(22)
lista.dodawanko(26) #
lista.dodawanko(256) #


lista.printowanko()

lista = funkcyjka(lista)
print('----')
lista.printowanko()

