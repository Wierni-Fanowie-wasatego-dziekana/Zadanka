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

def funkcja(p,q):
    counter=0
    ctp=p
    ctq=q
    while ctp is not None and ctq is not None:
        counter += 1
        ctp=ctp.next
        ctq=ctq.next
    flaga = True
    if ctp is None:
        flaga = False
    anotherp = p
    anotherq = q
    if flaga:
        while counter-1 > 0:
            anotherp=anotherp.next
            counter -= 1
    else:
        while counter-1 > 0:
            anotherq=anotherq.next
            counter -= 1
    anotherp.printowanko()
    print()
    anotherq.printowanko()
    print()
    cnt=0
    while anotherp is not None and anotherq is not None:
        if anotherp.val == anotherq.val:
            y = anotherp

            cnt+=1
        anotherp=anotherp.next
        anotherq=anotherq.next


    return cnt



lista = Node(2)  # To jest pańska ocena
lista.dodawanko(13)
lista.dodawanko(25)
lista.dodawanko(5)
lista.dodawanko(7)

lista2 = Node(3)  # To jest pańska ocena
lista2.dodawanko(5)
lista2.dodawanko(7)


print(funkcja(lista,lista2))
