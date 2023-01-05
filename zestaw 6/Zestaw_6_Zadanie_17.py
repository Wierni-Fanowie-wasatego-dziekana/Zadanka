""""". Dane są dwie liczby naturalne z których budujemy trzecią liczbę. W budowanej liczbie muszą wystąpić wszystkie cyfry występujące w liczbach wejściowych. Wzajemna kolejność cyfr każdej z liczb
wejściowych musi być zachowana. Na przykład mając liczby 123 i 75 możemy zbudować liczby 12375, 17523,
75123, 17253, itd. Proszę napisać funkcję która wyznaczy ile liczb pierwszych można zbudować z dwóch
zadanych liczb."""""
from math import log10
# 75123 -> 71523 -> 71253 -> 71235 -> 17523 -> 17253 -> 17235
#  12375 12735 12753 17235 17253
#
#
#
def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0 or n % 3 == 0:
        return False
    if n == 2 or n == 3:
        return True
    i = 5
    while i * i < n:
        if n % i == 0:
            return False
        i += 2
        if n % i == 0:
            return False
        i += 4
    return True



def lonczenie(liczba1, liczba2):
    length1 = int(log10(liczba1) + 1)
    length2 = int(log10(liczba2) + 1)

    napis1 = str(liczba1)
    napis2 = str(liczba2)

    for i in range(length1):
        for j in range(length2):
            nowy_napis += n
