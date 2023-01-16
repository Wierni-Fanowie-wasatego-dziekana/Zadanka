class Node:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next

    def dodawanko(self, T):
        p = self
        while p.next is not None:
            p = p.next
        for i in range(len(T)):
            p.next = Node(T[i])
            p = p.next

    def usuwanko(self, val):
        p = self
        while p.next.val != val and p.next is not None:
            p = p.next
        if p.next.val == val:
            p.next = p.next.next


    def obecnosciowanko(self,val):
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


lista = Node(None)
lista.dodawanko(5)
lista.dodawanko(6)
lista.dodawanko(7)
lista.printowanko()
lista.usuwanko(6)
lista.printowanko()
print(lista.obecnosciowanko(6))