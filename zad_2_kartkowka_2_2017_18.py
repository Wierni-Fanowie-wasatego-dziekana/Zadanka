'''Dana jest tablica t[N][N] (reprezentuj¡ca szachownic¦) wypierdolona liczbami naturalnymi. Na szachownicy
znajduj¡ si¦ dwie wie»e. Prosz¦ napisa¢ funkcj¦, która odpowiada na pytanie: czy istnieje ruch wie»¡
zwi¦kszaj¡cy sum¦ liczb na "szachowanych" przez wie»e polach? Do funkcji nale»y przekaza¢ tablic¦ oraz
poªo»enia dwóch wie», funkcja powinna zwróci¢ warto±¢ logiczn¡.
Uwaga: zakªadamy, »e wie»a szachuje caªy wiersz i kolumn¦ z wyª¡czeniem pola, na którym stoi.'''''

def sum_of_row(T,row,s = 0):
    for j in range(len(T)):
        s += T[row][j]
    return s
def sum_of_col(T,col,s = 0):
    for j in range(len(T)):
        s += T[j][col]
    return s

def sum_of_checked_places(T,a,b):
     sum_of_col, sum_of_row = 0, 0
     for j in range(len(T)):
         sum_of_col += T[j][b]
         sum_of_row += T[a][j]
     return sum_of_col + sum_of_row - 2 * T[a][b]

def sum_according_to_pos(T,row1,col1,row2,col2):
    if row1 == row2 and col1 != col2:
        return sum_of_row(T,row1) + sum_of_col(T,col1) + sum_of_col(T,col2) - 2 * T[row1][col1] - 2 * T[row2][col2]
    if row1 == row2 and col1 == col2:
        return 0
    if row1 != row2 and col1 == col2:
        return sum_of_col(T,col1) + sum_of_row(T,row1) + sum_of_row(T,row2) - 2 * T[row1][col1] - 2 * T[row2][col2]
    if row1 != row2 and col1 != col2:
        return sum_of_checked_places(T,row1,col1) + sum_of_checked_places(T,row2,col2) - T[row1][col2] - T[row2][col1]

def zadanko(T,row1,col1,row2,col2):
    s_max = sum_according_to_pos(T,row1,col1,row2,col2)

    if row1 == row2 and col2 > col1:
        for i in range(0,col2): # col 2 > col1
            for j in range(len(T)):
                if sum_according_to_pos(T,j,i,row2,col2) > s_max:
                    return True

        for i in range(col2,len(T)):
            for j in range(len(T)):
                if sum_according_to_pos(T,row1,col1,j,i) > s_max:
                    return True
    if col1 == col2 and row2 > row1:
        for i in range(0,row2): # col 2 > col1
            for j in range(len(T)):
                if sum_according_to_pos(T,i,j,row2,col2) > s_max:
                    return True

        for i in range(row2, len(T)):
            for j in range(len(T)):
                if sum_according_to_pos(T, row1, col1, i, j) > s_max:
                    return True
        if row1 < row2 and col1 < col2:
            for i in range(len(T)):
                for j in range(len(T)):
                    if sum_according_to_pos(T, i, j, row2, col2) > s_max:
                        return True
            for i in range(len(T)):
                for j in range(len(T)):
                    if sum_according_to_pos(T, row1, col1, i, j) > s_max:
                        return True

    return False 