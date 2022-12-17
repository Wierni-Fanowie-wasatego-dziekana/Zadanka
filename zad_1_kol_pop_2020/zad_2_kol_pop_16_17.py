'''Dana jest tablica booli int t[N][N] reprezentująca szachownicę. Pole szachownicy ma
wartość true, jeżeli stoi na nim figura, a false, jeśli jest ono puste. Proszę napisać
funkcję która sprawdza czy istnieje droga skoczka przemieszczającego się z wiersza
0 do wiersza N-1. Skoczek może poruszać się tylko po polach pustych. Skoczek w
każdym ruchu powinien przybliżać się do N-1 wiersza. Funkcja ma zwrócić
najmniejszą możliwą liczbę ruchów. Skoczek może zacząć poruszać się z dowolnego
pustego pola z wiersza 0. N z zakresu 4...20.'''

minimalna_ilsoc = float('inf')

def zadanie(T,w = 0, k = 0, ruchy = 0):
    global minimalna_ilsoc
    if w == len(T) - 1:
        minimalna_ilsoc = min(ruchy, minimalna_ilsoc)

    moves = [(2,1),(2,-1),(1,2),(1,-2)]

    for move in moves:
        next_w = w + move[0]
        next_k = k + move[1]
        if 0 <= next_w < len(T) and 0 <= next_k < len(T) and not T[next_w][next_k]:
            return zadanie(T, next_w, next_k, ruchy + 1)
    if minimalna_ilsoc == float('inf'):
        return False
    return minimalna_ilsoc

Szachownica = [[False,True,True,True,True],
               [True,True,False,True,True],
               [False,False,True,True,True],
               [True,False,True,False,True],
               [True,False,True,False,True]]

for i in range(len(Szachownica)): ### sprytrna zagrywka ###
    if not Szachownica[0][i]:
        zadanie(Szachownica, 0, i)

print(minimalna_ilsoc)