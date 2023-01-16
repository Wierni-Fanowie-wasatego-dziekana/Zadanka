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

def co_drugi(header, cnt = 0):
    while header.next is not None:
        if cnt % 2 == 0:
            header.next = header.next.next
        cnt += 1
        header = header.next


lista = Node(1)  # To jest pańska ocena     # Ale jak to jeden?
lista.dodawanko(2)
lista.dodawanko(3)
lista.dodawanko(4)
lista.dodawanko(5)
lista.dodawanko(6)
lista.dodawanko(7)
lista.dodawanko(8)
lista.dodawanko(9)
lista.printowanko()
lista.usuwankoost()

print()
lista.printowanko()