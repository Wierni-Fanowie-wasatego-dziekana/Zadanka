'''Dana jest N elementowy zbiór liczb naturalnych w postaci tablicy int t[N]. Proszę napisać
funkcję, która zwraca informację czy jest możliwy podział zbioru na trzy zbiory tak aby w każdym z
trzech zbiorów lączna liczba jedynek w liczbach zapisanych w systemie binarnym była jednakowa. Na
przykład dla zbioru |Ż,3,5,7,I1",L3,J-6} możliwy podział to {2,13,16} {3,11} {5,7} czyli w systemie
dwójkowym {10,1101,10000} {11,1011} {101,111} - w każdym zbiorze jest 5 jedynek.'''''


def dec_to_bin(n):
    counter = 0
    while n > 0:
        if n % 2 == 1:
            counter += 1
        n //= 2
    return counter

def zad_2(T, i=0, s1=0, s2=0, s3=0):
    if i == len(T):
        return s1 == s2 == s3

    return zad_2(T, i + 1, s1 + dec_to_bin(T[i]), s2, s3) or zad_2(T, i + 1, s1, s2 + dec_to_bin(T[i]),s3) or zad_2(T, i + 1, s1, s2, s3 + dec_to_bin(T[i]))

print(zad_2([2, 3, 5, 7, 11, 13, 16]))