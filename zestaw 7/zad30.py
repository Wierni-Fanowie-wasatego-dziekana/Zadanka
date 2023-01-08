'''
 Dane są dwie niepuste listy, z których każda zawiera niepowtarzające
się elementy. Elementy w pierwszej liście są uporządkowane rosnąco, w
drugiej elementy występują w przypadkowej kolejności. Proszę napisać
funkcję, która z dwóch takich list stworzy jedną, w której uporządkowane
elementy będą stanowić sumę mnogościową elementów z list wejściowych.
Do funkcji należy przekazać wskazania na obie listy, funkcja powinna
zwrócić wskazanie na listę wynikową. Na przykład dla list:
2 -> 3 -> 5 ->7-> 11
8 -> 2 -> 7 -> 4
powinna pozostać lista:
2 -> 3 -> 4 -> 5 ->7-> 8 -> 11
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


def studentsort(p,q):
    res = p
    g = p
    while q is not None:
        p = g
        flag = True
        while p.next is not None and p.next.val < q.val:
            p = p.next

        if p.next.val == q.val or p.val == q.val:
            flag = False
        if p.next is None:
            pom = Node(q.val)
            p.next = pom
            flag = False

        if flag:
            pom = Node(q.val)
            pom.next = p.next
            p.next = pom

        q = q.next

    return res


listunia = Node(2)
listunia.dodawanko(3)
listunia.dodawanko(5)
listunia.dodawanko(7)
listunia.dodawanko(11)
nielistunia=Node(8)
nielistunia.dodawanko(2)
nielistunia.dodawanko(7)
nielistunia.dodawanko(4)

listunia=studentsort(listunia, nielistunia)

listunia.printowanko()

