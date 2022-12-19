''' Dana jest tablica t[N][N] wypełniona liczbami całkowitymi.
Tablica reprezentuje szachownicę. Proszę napisać
funkcję, która sprawdza czy da się umieścić w każdym wierszu jednego króla szachowego tak aby 
żadne dwa króle nie stały w odległości mniejszej niż dwa ruchy króla. 
Dodatkowo, suma wartości pól zajmowanych przez wszystkie
figury była równa zero'''

def safe_pos(a,b,T):
    n=len(T)

flaga = False
def rozstawienie(T, poprzednia_kolumna=-1, poprzedniejsza_kolumna=-1, ilosc_zajetych_pol=0, suma=0):
    global flaga
    if ilosc_zajetych_pol == len(T) and suma == 0:
        flaga = True
        return True

    if poprzednia_kolumna == -1:
        for i in range(len(T)):
            rozstawienie(T, i, -1, ilosc_zajetych_pol+1 , suma + T[ilosc_zajetych_pol][i])
    elif poprzedniejsza_kolumna == -1 and poprzednia_kolumna != -1:
        for i in range(len(T)):
            if i < poprzednia_kolumna - 2 or i > poprzednia_kolumna + 2:
                rozstawienie(T, i, poprzednia_kolumna, ilosc_zajetych_pol + 1, suma + T[ilosc_zajetych_pol][i])
    else:
        for i in range(len(T)):
            if (i < poprzednia_kolumna - 2 and i < poprzedniejsza_kolumna - 2) or (i > poprzednia_kolumna + 2 and i > poprzedniejsza_kolumna + 2):
                rozstawienie(T, i, poprzednia_kolumna, ilosc_zajetych_pol + 1, suma + T[ilosc_zajetych_pol][i])

    return flaga



szachownica = [[-1, 7, 7, 7, 7, 7, 7],
               [ 7, 7, 7, 7, 7, 7,-1],
               [ 7, 7, 7,-1, 7, 7, 7],
               [-1, 7, 7, 7, 7, 7, 7],
               [ 7, 7, 7, 7, 7, 7,-1],
               [ 7, 7, 7,-1, 7, 7, 7],
               [ 6, 7, 7, 7, 7, 7, 7]]

boolowa_szachownica = [[True for _ in range(len(szachownica))] for _ in range(len(szachownica))]

print(rozstawienie(szachownica))