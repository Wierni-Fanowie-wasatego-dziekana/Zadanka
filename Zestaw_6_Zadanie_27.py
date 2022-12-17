"""Kwadrat jest opisywany czwórką liczb całkowitych (x1, x2, y1, y2), gdzie x1, x2, y1, y2 oznaczają proste ograniczające kwadrat x1 < x2, y1 < y2. Dana jest tablica T zawierająca opisy N kwadratów. Proszę
napisać funkcję, która zwraca wartość logiczną True, jeśli danej tablicy można znaleźć 13 nienachodzących
na siebie kwadratów, których suma pól jest równa 2012 i False w przeciwnym przypadku."""""
from random import randint
def grzeszczuk(x):
    return (x[0]-x[1])**2



def karatkevich():
    pass

lista=[]
listunia = []

def gajecki(T,listunia, sum=0,i=0, num_of_squares=0):
    global lista
    if sum == 2012 and num_of_squares == 13:
        lista.append(listunia)

    kopia = listunia.copy()
    kopia.append(T[i])
    return gajecki(T,kopia, sum + grzeszczuk(T[i]), i + 1, num_of_squares + 1) or gajecki(T,listunia, sum, i + 1, num_of_squares)

tabliczka = []

for i in range(500):
    randomowa1 = randint(1, 100)
    randomowa2 = randint(1,100)
    randomowa_suma = randint(1,45)
    tabliczka.append((randomowa1, randomowa1+randomowa_suma, randomowa2, randomowa2+randomowa_suma))

# Tablica = [(randint(1,100),randint(1,100),0,0) for _ in range(105)]
#
# def kurwa_mac(Tablica):
#     randint
# Tablica2 = [grzeszczuk(Tablica[i]) for i in range(len(Tablica))]
# Tablica3=[]
# for r in Tablica2:
#     print(r)
# for r in Tablica:
#     print(r)

listunia = []
gajecki(tabliczka, listunia)