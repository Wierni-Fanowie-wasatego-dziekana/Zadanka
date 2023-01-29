'''Na szachownicy o rozmiarach N × N reprezentowanej przez tablicę T[N][N] umieszczono pewną liczbę
skoczków. Położenie skoczka w tablicy oznaczono liczbą 1, puste pola oznaczono liczbą 0. Część pustych pól
na szachownicy jest szachowana przez znajdujące się na niej skoczki. Proszę zaproponować funkcję place(T),
która znajdzie na szachownicy puste pole położone najbliżej środka szachownicy, takie że umieszczenie tam
skoczka maksymalnie zwiększy liczbę szachowanych pustych pól. Do funkcji przekazujemy tablicę T zawierającą położenie skoczków. Funkcja powinna zwrócić pole (wiersz, kolumna), na którym należy umieścić
skoczka. Odległość pomiędzy polami: (w1, k1) i (w2, k2) jest równa max(abs(w1 − w2), abs(k1 − k2))'''''

def sum_of_checked(T, w, k, if_first):
    if not if_first:
        T[w][k] = 1

    N = len(T)
    moves = [(2,1),(2,-1),(1,2),(-1,2),(1,-2),(-1,-2),(-2,1),(-2,-1)]
    suma = 0
    for w in range(N):
        for k in range(N):
            if T[w][k] == 1:
                suma += 1
                for move in moves:
                    if 0 <= w + move[0] < N and 0 <= k + move[1] < N:
                        if not T[w + move[0]][k + move[1]] == 1 or not T[w + move[0]][k + move[1]] == 2:
                            suma += 1
                            T[w + move[0]][k + move[1]] = 2
    return suma

def distance(a,b,c):
    return max(abs(a - b), abs(a - c))

def place(T):
    N = len(T)
    curr_sum = sum_of_checked(T, 0, 0, True)
    min_dist = float('inf')
    center = ( N // 2 ) + 1
    for w in range(N):
        for k in range(N):
            if T[w][k] == 0:
                temp_sum = sum_of_checked(T,w,k,False)
                temp_dist = distance(center, w, k)
                if temp_sum > curr_sum:
                    curr_sum = temp_sum
                    min_dist = temp_dist
                    placement = (w,k)
                elif temp_sum == curr_sum:
                    if min_dist > temp_dist:
                        placement = (w,k)
                        min_dist = temp_dist

    return placement


T = [
    [0,1,0],
    [0,0,0],
    [0,0,0],

]

print(place(T))