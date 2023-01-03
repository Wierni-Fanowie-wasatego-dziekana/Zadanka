'''Dana jest tablica t[N] zawierająca liczby naturalne. Proszę napisać funkcję, która odpowiada na pytanie,
czy z elementów tablicy (niekoniecznie wszystkich) można utworzyć dwa równoliczne, niepuste podzbiory
o jednakowej sumie elementów. Do funkcji należy przekazać wyłącznie tablicę t, funkcja powinna zwrócić
wartość typu bool.'''''


def zadanko(T, i = 0, s1 = 0, s2 = 0, ile_elementow1= 0, ile_elementow2 = 0):
    if i >= len(T):
        return False

    if ile_elementow1 == ile_elementow2 and s1 == s2 and ile_elementow1 > 0:
        return True

    return zadanko(T,i+1,s1+T[i],s2,ile_elementow1+1,ile_elementow2) or zadanko(T,i+1,s1,s2+T[i],ile_elementow1,ile_elementow2+1) or  zadanko(T,i+1,s1,s2,ile_elementow1,ile_elementow2)

T = [1, 6, 38, 2, 5]

print(zadanko(T))