'''2. Na zbiorze liczb całkowitych określono trzy operacje: A,B,C przekształcające liczby:
 A: zwiększa liczbę o 3;
 B: podwaja liczbę;
 C: wszystkie parzyste cyfry w liczbie zwiększa o 1, np. 2356->3357, 1999->1999.
Proszę napisać funkcję która sprawdza czy można przekształcić liczbę X na liczbę Y w nie więcej niż N krokach.
Do funkcji należy przekazać wartości X,Y,N, funkcja powinna zwrócić liczbę możliwych ciągów operacji
przekształcających liczbę X w Y (lub wartość 0 jeżeli takie przekształcenie nie istnieje). Uwaga: zabronione jest
używanie kolejno dwóch tych samych operacji.
Na przykład:
Dla X=11, Y=31, N=4 funkcja powinna zwrócić 3 bo są 3 możliwe ciągi operacji: ABA, ACBC, CABA
Dla X=11, Y=32, N=4 funkcja powinna zwrócić 0.'''''

def operacja_A(liczba):
    return liczba + 3

def operacja_B(liczba):
    return 2 * liczba

def operacja_C(liczba):
    kopia = liczba
    i = 0
    while kopia > 0:
        if (kopia % 10) % 2 == 0:
            liczba += 1 * 10**i
        kopia = kopia // 10
        i+=1
    return liczba

mozliwosci = 0


def transfer(liczba_poczatkowa, liczba_docelowa, liczba_krokow, i=0, ostatni_wybryk=None, stringus=''):
    global mozliwosci
    if i > liczba_krokow:
        return False

    if liczba_poczatkowa == liczba_docelowa:
        mozliwosci += 1
        print(stringus)

    if ostatni_wybryk is None:
        transfer(operacja_A(liczba_poczatkowa), liczba_docelowa, liczba_krokow, i+1, 'A', stringus + 'A')
        transfer(operacja_B(liczba_poczatkowa), liczba_docelowa, liczba_krokow, i+1, 'B', stringus + 'B')
        transfer(operacja_C(liczba_poczatkowa), liczba_docelowa, liczba_krokow, i+1, 'C', stringus + 'C')

    elif ostatni_wybryk == 'A':
        transfer(operacja_B(liczba_poczatkowa), liczba_docelowa, liczba_krokow, i + 1, 'B', stringus + 'B')
        transfer(operacja_C(liczba_poczatkowa), liczba_docelowa, liczba_krokow, i + 1, 'C', stringus + 'C')

    elif ostatni_wybryk == 'B':
        transfer(operacja_A(liczba_poczatkowa), liczba_docelowa, liczba_krokow, i + 1, 'A', stringus + 'A')
        transfer(operacja_C(liczba_poczatkowa), liczba_docelowa, liczba_krokow, i + 1, 'C', stringus + 'C')

    elif not liczba_poczatkowa == operacja_C(liczba_poczatkowa):
        transfer(operacja_A(liczba_poczatkowa), liczba_docelowa, liczba_krokow, i + 1, 'A', stringus + 'A')
        transfer(operacja_B(liczba_poczatkowa), liczba_docelowa, liczba_krokow, i + 1, 'B', stringus + 'B')


transfer(3, 45, 15)
print(mozliwosci)