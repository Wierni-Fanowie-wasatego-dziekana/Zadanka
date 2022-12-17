''''Dana jest tablica T zawierająca liczby wymierne reprezentowane w postaci ułamków. Ułamki reprezentowane
są w postaci krotek składających się z licznika i mianownika. Proszę napisać funkcję longest(T), zwracającą
długość najdłuższego spójnego podciągu, którego elementy stanowią ciąg geometryczny. W przypadku gdy
w tablicy nie ma ciągu dłuższego niż 2 elementy, funkcja powinna zwrócić wartość 0.
Komentarz: Można założyć, że tablica wejściowa liczy więcej niż 2 elementy.
Przykłady:
print(longest( [(0,2),(1,2),(2,2),(4,2),(4,1),(5,1)] ) # wypisze 4
print(longest( [(1,2),(-1,2),(1,2),(1,2),(1,3),(1,2)] ) # wypisze 3
print(longest( [(3,18),(-1,6),(7,42),(-1,6),(5,30),(-1,6)] ) # wypisze 6
print(longest( [(1,2),(2,3),(3,4),(4,5),(5,6)] ) # wypisze 0 '''''

def krota_do_liczby(krotka):
    return krotka[0]/krotka[1]

def znajdz_najdluzszy_ciag(T):
    j = 1
    while krota_do_liczby(T[j-1]) == 0:
        j += 1
    q = krota_do_liczby(T[j])/krota_do_liczby(T[j-1])
    dl = 1
    najdluzszy = -1
    for i in range(1, len(T)):
        if krota_do_liczby(T[i - 1]) != 0:
            if krota_do_liczby(T[i]) / krota_do_liczby(T[i - 1]) == q:
                dl += 1
            else:
                q=krota_do_liczby(T[i])/krota_do_liczby(T[i-1])
                if dl > najdluzszy:
                    najdluzszy = dl
                dl = 1
    if dl > najdluzszy:
        najdluzszy = dl
    if najdluzszy > 2:
        return najdluzszy
    return 0

print(znajdz_najdluzszy_ciag([(0,2),(1,2),(2,2),(4,2),(4,1),(5,1)]))
print(znajdz_najdluzszy_ciag([(1,2),(-1,2),(1,2),(1,2),(1,3),(1,2)]))
print(znajdz_najdluzszy_ciag([(3,18),(-1,6),(7,42),(-1,6),(5,30),(-1,6)]))
print(znajdz_najdluzszy_ciag([(1,2),(2,3),(3,4),(4,5),(5,6)]))