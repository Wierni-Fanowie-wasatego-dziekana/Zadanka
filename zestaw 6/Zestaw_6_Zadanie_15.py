def possible(grid, y, x):  # is it possible to place a queen into y,x?

    l = len(grid)  # how big is our grid?

    for i in range(l):  # check for queens on row y
        if grid[y][i] == 0:  # if exist return false
            return False
    for i in range(l):
        if grid[i][x] == 0:
            return False

    for i in range(l):
        for j in range(l):
            if grid[i][j] == 0:
                if abs(i - y) == abs(j - x):
                    return False
    return True

def Hetman_Zamoyski(T):
    for i in range(len(T)):
        for j in range(len(T)):
            if T[i][j]:
                if possible(T,i,j):
                    T[i][j] = 0
                    Hetman_Zamoyski(T)
                    suma=0
                    for y in range(len(T)):
                        for x in range(len(T)):
                            if T[y][x]==0:
                                suma+=1
                    if suma == 8:
                        return T
                    T[i][j]=1


    return T

T = [[1 for _ in range(8)] for _ in range(8)]

tablica = Hetman_Zamoyski(T)

for r in tablica:
    print(r)