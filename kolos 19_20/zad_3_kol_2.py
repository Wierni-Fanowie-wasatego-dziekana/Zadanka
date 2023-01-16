'''Kolejne (co najmniej dwa) elementy listy o identycznej wartości pola val nazywamy podlistą stałą. Proszę napisać
funkcję, która usuwa z listy wejściowej najdłuższą podlistę stałą. Warunkiem jej usunięcia jest istnienie w liście
dokładnie jednej najdłuższej podlisty stałej. Do funkcji należy przekazać wskaźnik na pierwszy element listy.
Funkcja powinna zwrócić liczbę usuniętych elementów'''

class Node:
    def __init__(self, val=None, next = None):
        self.val = val
        self.next = next

    def karatkevich(self, val):
        p = self
        while p.next is not None:
            p = p.next
        p.next = Node(val)

    def grzeszczuk(self):
        q = self
        while q is not None:
            print(q.val)
            q = q.next



def KYS(header):
    p = header
    q=header
    obecnadl=1
    najdluzsze=0
    while p.next is not None:
        if p.val == p.next.val:
            if obecnadl == 1:
                wskaznik = p
            obecnadl+=1
            p=p.next
        else:
            if obecnadl>najdluzsze:
                najdluzsze, obecnadl = obecnadl, 1
                maxwskaznik = wskaznik
            p=p.next
    if obecnadl > najdluzsze:
        najdluzsze, obecnadl = obecnadl, 1
        maxwskaznik=wskaznik
    while maxwskaznik.next is not None and maxwskaznik.val == maxwskaznik.next.val:
        maxwskaznik.next=maxwskaznik.next.next
    while q.next is not maxwskaznik:
        q=q.next
    q.next=q.next.next
    return najdluzsze


def funkcyjka(head):
    p, res = head, head
    indeks_max, cnt, max_cnt, i = 1, 1, 1, 0
    while p.next is not None:
        if p.next.val > p.val:
            w_start = p
            while w_start.next is not None and w_start.next.val > w_start.val:
                w_start = w_start.next
                cnt += 1
            if cnt > max_cnt:
                indeks_max = i
                max_cnt = cnt
            cnt = 1
        p = p.next
        i += 1

    q = res
    for i in range(indeks_max - 1):
        res = res.next
    for j in range(max_cnt):
        res.next = res.next.next

    return q

garek = Node(2)
garek.karatkevich(2)
garek.karatkevich(2)
garek.karatkevich(2)
garek.karatkevich(3)
garek.karatkevich(2)
garek.karatkevich(2)
garek.karatkevich(4)
garek.karatkevich(2)
garek.karatkevich(6)
garek.karatkevich(6)
garek.karatkevich(6)
garek.karatkevich(6)
garek.karatkevich(6)
garek.karatkevich(3)
garek.karatkevich(3)
garek.karatkevich(3)
garek.karatkevich(3)
garek.karatkevich(3)
garek.karatkevich(3)
#garek.karatkevich(None)
KYS(garek)
print('---')
liczba = KYS(garek)
print(liczba)
print()
garek.grzeszczuk()

