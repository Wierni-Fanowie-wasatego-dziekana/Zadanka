'''Dana jest liczba naturalna N. Proszę zaimplementować funkcję divide(N), która sprawdza czy jest możliwe
pocięcie liczby N na kawałki, tak aby każdy z kawałków był liczba pierwszą oraz liczba kawałków też była
liczbą pierwszą. Funkcja powinna zwracać wartość logiczną. Na przykład: divide(2347)=True, podział na
23 i 47, natomiast divide(2255)=False.'''''

from math import log10

def is_prime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i < n:
        if n % i == 0:
            return False
        i += 2
        if n % i == 0:
            return False
        i += 4

    return True


def divide(N, licza_podzialow = 0):
    print(N,licza_podzialow)
    if N == 0:
        print(licza_podzialow)
        return is_prime(licza_podzialow)
    ile_cyfr = int(log10(N))+1
    for i in range(1, ile_cyfr+1):
        odciecie_z_przodu=N//(10**(ile_cyfr-i))
        nowe_n=N%(10**(ile_cyfr-i))
        if is_prime(odciecie_z_przodu) and divide(nowe_n,licza_podzialow+1):
            return True

    return False

#gotowe
# CHUJA GOTOWE
print(divide(2255))