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

    def usuwankoost(self):
        q = self
        while q is not None and q.next is not None:
            q.next = q.next.next
            q = q.next


lista = Node(2)  # To jest pańska ocena
lista.dodawanko(997)
lista.dodawanko(213)
lista.dodawanko(2115)
lista.dodawanko(420)
lista.printowanko()

lista.usuwankoost()

print()
lista.printowanko()