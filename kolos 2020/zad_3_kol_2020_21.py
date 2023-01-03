'''Dana jest tablica T[N][N] (reprezentująca szachownicę) wypełniona liczbami całkowitymi. Proszę zaimplementować funkcję chess(T) która ustawia na szachownicy dwie wieże, tak aby suma liczb na
„szachowanych” przez wieże polach była największa. Do funkcji należy przekazać tablicę, funkcja powinna
zwrócić położenie wież w postaci krotki (row1, col1, row2, col2).
Uwaga: zakładamy, że pola na których znajdują się wieże nie są szachowane.'''''

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

def chess(T,s_max = -1, coordinates = None):
    for i in range(len(T)):
        for j in range(len(T)):
            for k in range(len(T)):
                for l in range(len(T)):
                    if sum_according_to_pos(T,i,j,k,l) > s_max:
                        coordinates = (i,j,k,l)
                        s_max = sum_according_to_pos(T,i,j,k,l)

    return coordinates

print(chess([[4,0,2],[3,0,0],[6,5,3]]))
print(chess([[1,1,2,3],[-1,3,-1,4], [4,1,5,4], [5,0,3,6]]))


