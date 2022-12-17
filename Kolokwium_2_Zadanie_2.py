def find_empty_spaces(T):
    for row in range(len(T)):
        for col in range(len(T)):
            x = col
            if T[col][row]:
                x = -1
                break
        if True not in T[row] and x != -1:
            return row, x

def find_perfect_rook(T):
    n = len(T)
    another_in_row = False
    another_in_column = False
    for i in range(n):
        for j in range(n):
            if T[i][j]:
                for k in range(n):
                    if T[i][k]:
                        if k != j:
                            another_in_row = True
                    if T[k][j]:
                        if k != i:
                            another_in_column = True
                if another_in_row and another_in_column:
                    return i, j
                another_in_column = False
                another_in_row = False
    return None

def move(T):
    return (f'wspolrzedne poczatkowe wiezy wynosza {find_perfect_rook(T)}, natomiat wspolrzedne docelowe wynosza {find_empty_spaces(T)}')

Tab = [[True, False, False, False],
       [False, False, False, False],
       [True, False, False, False],
       [True, False, False, True]]

print(move(Tab))
