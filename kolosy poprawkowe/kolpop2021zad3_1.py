'''Lista zawierała wartości stanowiące kolejne wyrazy ciągu arytmetycznego. Z wnętrza listy usunięto
pewną liczbę elementów. Proszę napisać funkcję repair(p), (p wskazuje na pierwszy element listy) która
uzupełnia listę elementami, tak aby ponownie zawierała kolejne wyrazy ciągu arytmetycznego. Funkcja
powinna zwrócić liczbę wstawionych elementów.'''

class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

    def dodawanko(self, val):
        p = self
        while p.next is not None:
            p = p.next
        p.next = Node(val)

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
    def usuwanko(self, val):
        p = self
        while p.next is not None:
            if p.next.val == val:
                p.next = p.next.next

def NWD(a,b):
    while b != 0:
        a, b = b, a % b
    return a

def repair(p):
    q = p
    r = p.next.val - p.val

    while p.next is not None:
        curr_r = p.next.val - p.val
        r = NWD(curr_r, r)
        p = p.next

    q_start = q
    while q.next is not None:
        if not q.val + r == q.next.val:
            q.next = Node(q.val+r, q.next)
        q = q.next

    return q_start


lista = Node(22)  # wartownik
lista.dodawanko(16) # To jest pańska ocena
lista.dodawanko(10) # O tej ocenie możesz porozmawiać pod biurkiem
lista.dodawanko(-2)


lista2 = Node(0)
lista2.dodawanko(2) # To jest pańska ocena
lista2.dodawanko(3)
lista2.dodawanko(13)
lista2.dodawanko(24)
#lista2.dodawanko(25)

listuuunia = repair(lista)
listuuunia.printowanko()