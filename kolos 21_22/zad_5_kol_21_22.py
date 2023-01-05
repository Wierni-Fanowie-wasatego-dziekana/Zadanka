'''Dwie liczby naturalne są czynnikowo-podobne, jeżeli w swoich rozkładach na czynniki pierwsze mają
dokładnie jeden czynnik równy. Na przykład: 24 i 14 albo 32 i 18. Dana jest tablica T[N][N]
zawierająca liczby naturalne. Dwie liczby sąsiadują ze sobą wtedy, gdy leżą w sąsiednich kolumach i
sąsiednich wiersza. Proszę napisać funkcję three(T), która zwraca ilość liczb w tablicy sąsiadujących
dokładnie z 3 liczbami czynnikowo-podobnymi.'''''

def czy_czynnikowo_podobne(liczba1, liczba2):
    i, counter = 2, 0
    while liczba1 != 1:
        while liczba1 % i == 0:
            liczba1 /= i
            if liczba2 % i == 0:
                counter += 1
                liczba2 //= i
        if counter > 1:
            return False
        i += 1
    return True

def three(T):
    n = len(T)
    counter = 0
    ilosc_sasiadow = 0
    for i in range(1,n-1):
        for j in range(1,n-1):
            ilosc_sasiadow = 0
            if czy_czynnikowo_podobne(T[i][j],T[i-1][j]):
                ilosc_sasiadow+=1
            if czy_czynnikowo_podobne(T[i][j],T[i+1][j]):
                ilosc_sasiadow+=1
            if czy_czynnikowo_podobne(T[i][j],T[i][j-1]):
                ilosc_sasiadow+=1
            if czy_czynnikowo_podobne(T[i][j],T[i][j+1]):
                ilosc_sasiadow+=1
            if ilosc_sasiadow==3:
                counter+=1

    for i in range(1,n-1):  #Sprawdzanie lewego boku
        if czy_czynnikowo_podobne(T[i][0],T[i-1][0]):
            ilosc_sasiadow+=1
        if czy_czynnikowo_podobne(T[i][0],T[i][1]):
            ilosc_sasiadow+=1
        if czy_czynnikowo_podobne(T[i][0],T[i+1][0]):
            ilosc_sasiadow+=1
        if ilosc_sasiadow == 3:
            counter += 1
        ilosc_sasiadow = 0

    for i in range(1,n-1):  #Sprawdzanie prawego boku
        if czy_czynnikowo_podobne(T[i][n-1],T[i-1][n-1]):
            ilosc_sasiadow+=1
        if czy_czynnikowo_podobne(T[i][n-1],T[i][n-2]):
            ilosc_sasiadow+=1
        if czy_czynnikowo_podobne(T[i][n-1],T[i+1][n-1]):
            ilosc_sasiadow+=1
        if ilosc_sasiadow == 3:
            counter += 1
        ilosc_sasiadow = 0

    for i in range(1,n-1):  #Sprawdzanie gornego boku
        if czy_czynnikowo_podobne(T[0][i],T[0][i-1]):
            ilosc_sasiadow+=1
        if czy_czynnikowo_podobne(T[0][i],T[1][i]):
            ilosc_sasiadow+=1
        if czy_czynnikowo_podobne(T[0][i],T[0][i+1]):
            ilosc_sasiadow+=1
        if ilosc_sasiadow == 3:
            counter += 1
        ilosc_sasiadow = 0

    for i in range(1, n - 1):  # Sprawdzanie gornego boku
        if czy_czynnikowo_podobne(T[n-1][i], T[n-1][i - 1]):
            ilosc_sasiadow += 1
        if czy_czynnikowo_podobne(T[n-1][i], T[n-2][i]):
            ilosc_sasiadow += 1
        if czy_czynnikowo_podobne(T[n-1][i], T[n-1][i + 1]):
            ilosc_sasiadow += 1
        if ilosc_sasiadow == 3:
            counter += 1
        ilosc_sasiadow = 0

    return counter


