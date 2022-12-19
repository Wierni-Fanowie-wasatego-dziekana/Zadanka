'''Punkt leżący na płaszczyźnie jest opisywany parą liczb typu float (x,y). Tablica T[N] zawiera
współrzędne N punktów leżących na płaszczyźnie. Punkty posiadają jednostkową masę. Proszę napisać funkcję, 
która sprawdza czy istnieje niepusty podzbiór n punktów, gdzie n<=k oraz n jest wielokrotnością liczby
3, którego środek ciężkości leży w odległości mniejszej niż r od początku układu współrzędnych. Do funkcji
należy przekazać dokładnie 3 parametry: tablicę t, promień r, oraz ograniczenie k, funkcja powinna zwrócić
wartość typu bool.'''''

def odleglosc_mniejsza_od_r(n,r):
    dl = (n[0]**2 + n[1]**2)**0.5
    return dl < r

def srodek_ciezkosci(T):
    sc=[0,0]
    for i in range(len(T)):
        sc[0]+=T[i][0]
        sc[1]+=T[i][1]
    sc[0]/=len(T)
    sc[1]/=len(T)

    return sc

def wielokrotnosc_trojki(n):
    return n % 3 == 0

def zad30(T,r,k, srodeczek, i = 0):
    if len(srodeczek) > k or i >= len(T):
        return False
    if 0 < len(srodeczek) <= k and odleglosc_mniejsza_od_r(srodek_ciezkosci(srodeczek), r):
        return wielokrotnosc_trojki(len(srodeczek))

    if zad30(T,r,k,srodeczek, i+1):
        return True
    srodeczek.append(T[i])
    return zad30(T,r,k,srodeczek,i+1)


Punkciory = [(1,1),(-1,1),(-1,-1),(1,-1)]
srouda_dzien_louda = []

print(zad30(Punkciory,2,5,srouda_dzien_louda))